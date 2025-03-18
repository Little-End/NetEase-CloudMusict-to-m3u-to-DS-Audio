def convert_to_m3u_format(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for idx, line in enumerate(infile, start=1):
            raw_line = line.strip()
            if not raw_line:
                continue  # 跳过空行

            # 尝试分割标题和艺术家（反顺序）
            if ' - ' in raw_line:
                title, artist = raw_line.split(' - ', 1)  # 分割顺序调换
            else:
                # 格式不正确的行：整行作为标题，艺术家设为 Unknown
                title = raw_line
                artist = "@@@@@@@@@@@@@@@@@@@@"

            # 安全处理文件名中的斜杠
            safe_artist = artist.replace('/', ',')
            safe_title = title.replace('/', ',')

            # 写入结果（保留原始内容，仅修改路径部分）
            outfile.write(f"#EXTINF:{idx},{artist} - {title}\n")  # 保留原始内容
            outfile.write(f"/music/{safe_title} - {safe_artist}.mp3\n")  # 路径顺序调换

# 示例调用
convert_to_m3u_format('songs.txt', 'playlist.m3u')
