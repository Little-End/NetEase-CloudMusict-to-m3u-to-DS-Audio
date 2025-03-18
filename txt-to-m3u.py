def convert_to_m3u_format(input_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        # 读取第一行并提取播放列表名称
        first_line = infile.readline().strip()
        if first_line.startswith("====") and first_line.endswith("===="):
            playlist_name = first_line[4:-4].strip()  # 提取 ====Trap==== 中的 Trap
        else:
            playlist_name = "DefaultPlaylist"  # 如果格式不正确，使用默认名称

        # 动态生成输出文件名
        output_file = f"{playlist_name}.m3u"

        with open(output_file, 'w', encoding='utf-8') as outfile:
            # 写入 M3U 文件头部
            outfile.write("#EXTM3U\n")
            outfile.write(f"#PLAYLIST:{playlist_name}\n")

            # 重置文件指针，重新读取文件内容
            infile.seek(0)
            next(infile)  # 跳过第一行

            for idx, line in enumerate(infile, start=1):
                raw_line = line.strip()
                if not raw_line or raw_line.startswith("===="):
                    continue  # 跳过空行和以 ==== 开头的行

                # 尝试分割标题和艺术家
                if ' - ' in raw_line:
                    parts = raw_line.split(' - ', 1)
                    title = parts[0].strip()
                    artist = parts[1].strip() if parts[1].strip() else "@@@@@@@@@@@@@@@@@@@"
                else:
                    # 格式不正确的行：整行作为标题，艺术家设为 Unknown
                    title = raw_line
                    artist = "@@@@@@@@@@@@@@@@@@@"

                # 安全处理文件名中的斜杠
                safe_artist = artist.replace('/', ',')
                safe_title = title.replace('/', ',')

                # 写入结果
                outfile.write(f"#EXTINF:{idx},{artist} - {title}\n")
                outfile.write(f"/music/{safe_title} - {safe_artist}.mp3\n")

    print(f"Playlist '{playlist_name}' has been saved to '{output_file}'.")

# 示例调用
convert_to_m3u_format('songs.txt')
