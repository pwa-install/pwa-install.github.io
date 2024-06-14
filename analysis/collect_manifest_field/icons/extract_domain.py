import re


def extract_domains(url_line):
    urls = url_line.split(", ")
    domain_icon = None
    domain_urls = []

    # 提取第一个URL作为icon的URL
    first_url = urls[0]
    if "https" in first_url:
        domain_icon = re.findall(r"https://[^\s/]*", first_url)[0]
        domain_icon = domain_icon.replace("https://", "")
        domain_icon_parts = domain_icon.split(".")
        if len(domain_icon_parts) > 2:
            domain_icon = ".".join(domain_icon_parts[-2:])
        else:
            domain_icon = ".".join(domain_icon_parts)

    # 提取其它URL作为domain URLs
    for u in urls[1:]:
        if u.strip():  # 确保不处理空字符串
            domain_url = u.strip()
            domain_url_parts = domain_url.split(".")
            if len(domain_url_parts) > 2:
                domain_url = ".".join(domain_url_parts[-2:])
            else:
                domain_url = ".".join(domain_url_parts)
            domain_urls.append(domain_url)

    return domain_icon, domain_urls


with open("output_file2.txt", "r") as f:
    with open("potential_vulnerable.txt", "w") as r:
        written_records = set()  # 用于存储已经写入的记录
        for line in f:
            # 调用函数
            icon, urls = extract_domains(line)
            different_urls = [
                url for url in urls if url != icon
            ]  # 收集不等于icon的URLs
            if different_urls:  # 如果有不相同的URLs存在
                record = f"{icon}, {different_urls}\n"
                if record not in written_records:  # 检查记录是否已经写入过
                    r.write(record)
                    written_records.add(record)  # 添加到已写入记录的集合中
