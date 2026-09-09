import os

GA_MEASUREMENT_ID = "G-XQHCKTLW9Q"

GA_SNIPPET = f"""\t<!-- Google tag (gtag.js) -->
\t<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
\t<script>
\t  window.dataLayer = window.dataLayer || [];
\t  function gtag(){{dataLayer.push(arguments);}}
\t  gtag('js', new Date());

\t  gtag('config', '{GA_MEASUREMENT_ID}');
\t</script>
</head>"""

def inject_analytics(start_dir="."):
    processed_files = 0
    skipped_files = 0

    for root, _, files in os.walk(start_dir):
        for file in files:
            if file.lower().endswith(".html"):
                filepath = os.path.join(root, file)

                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # Пропускаем, если тег уже есть
                if GA_MEASUREMENT_ID in content:
                    skipped_files += 1
                    continue

                if "</head>" in content:
                    new_content = content.replace("</head>", GA_SNIPPET, 1)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    processed_files += 1
                else:
                    print(f"[!] Тег </head> не найден: {filepath}")

    print(f"\nГотово!")
    print(f" - Обновлено файлов: {processed_files}")
    print(f" - Уже содержали тег (пропущено): {skipped_files}")

if __name__ == "__main__":
    inject_analytics()