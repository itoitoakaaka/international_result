import pandas as pd
import xml.etree.ElementTree as ET
import sys
import os


def main():
    # XMLファイルのパスをコマンドライン引数から取得
    if len(sys.argv) < 2:
        print("使い方: python international_result.py <XMLファイルパス>")
        print("例: python international_result.py data.xml")
        sys.exit(1)
    file_path = sys.argv[1]
    tree = ET.parse(file_path)
    root = tree.getroot()

    # ATHLETEのENTRYと結果・準決勝・決勝を分けてデータを抽出する処理
    athletes_entries_finals_results = []

    for athlete in root.findall(".//ATHLETE"):
        for entry in athlete.findall(".//ENTRY"):
            # ENTRYの基本情報をディクショナリに格納
            entry_data = {
                "athleteid": athlete.get("athleteid"),
                "lastname": athlete.get("lastname"),
                "firstname": athlete.get("firstname"),
                "gender": athlete.get("gender"),
                "birthdate": athlete.get("birthdate"),
                "entrytime": entry.get("entrytime"),
                "eventid": entry.get("eventid"),
                "heat": entry.get("heat"),
            }

            # 日付情報
            meetinfo = entry.find(".//MEETINFO")
            if meetinfo is not None and meetinfo.get("date"):
                entry_data["meet_date"] = meetinfo.get("date")

            # 準決勝のRESULTを抽出
            pre_final_eventid = entry_data["eventid"]
            semi_final_result = athlete.find(f'.//RESULT[@eventid="{pre_final_eventid}"]')
            if semi_final_result is not None:
                split_50 = semi_final_result.find('.//SPLIT[@distance="50"]')
                split_100 = semi_final_result.find('.//SPLIT[@distance="100"]')
                entry_data["semi_final_splittime"] = split_50.get("swimtime") if split_50 is not None else None
                entry_data["semi_final_laptime"] = split_100.get("swimtime") if split_100 is not None else None
                entry_data["semi_final_place"] = semi_final_result.get("place")
            else:
                entry_data["semi_final_splittime"] = None
                entry_data["semi_final_laptime"] = None
                entry_data["semi_final_place"] = None

            # 決勝のRESULTを抽出
            final_eventid = entry_data["eventid"]
            final_result = athlete.find(f'.//RESULT[@eventid="{final_eventid}"]')
            if final_result is not None:
                split_50 = final_result.find('.//SPLIT[@distance="50"]')
                split_100 = final_result.find('.//SPLIT[@distance="100"]')
                entry_data["final_splittime"] = split_50.get("swimtime") if split_50 is not None else None
                entry_data["final_laptime"] = split_100.get("swimtime") if split_100 is not None else None
                entry_data["final_place"] = final_result.get("place")
            else:
                entry_data["final_splittime"] = None
                entry_data["final_laptime"] = None
                entry_data["final_place"] = None

            athletes_entries_finals_results.append(entry_data)

    # CSVファイルとして出力
    csv_path = "athletes_entries_finals_results.csv"
    df = pd.DataFrame(athletes_entries_finals_results)
    df.to_csv(csv_path, index=False)
    print(f"✅ CSV保存完了: {csv_path}")


if __name__ == "__main__":
    main()