##Problem 2:
#partial answer - failed
def format_newspaper_page(paragraphs, width):
    def center_text(text, line_width):
        spaces_needed = line_width - len(text)
        if spaces_needed % 2 == 0:
            spaces_before = spaces_needed // 2
            spaces_after = spaces_before
        else:
            spaces_before = spaces_needed // 2
            spaces_after = spaces_before + 1
        return " " * spaces_before + text + " " * spaces_after

    result = []
    border = '*' * (width + 2)
    result.append(border)

    for paragraph in paragraphs:
        i = 0
        while i < len(paragraph):
            line = paragraph[i]
            j = i + 1
            while j < len(paragraph) and len(line) + len(paragraph[j]) + (j - i) <= width:
                line += " " + paragraph[j]
                j += 1
            line = line.strip()
            if j == i + 1 or j == len(paragraph):
                line = center_text(line, width)
            else:
                spaces = width - len(line)
                spaces_between_words = spaces // (j - i - 1)
                extra_spaces = spaces % (j - i - 1)
                line = (" " * (spaces_between_words + 1)).join(line.split())
                for k in range(extra_spaces):
                    line = line[:k * (spaces_between_words + 1) + k + 1] + " " + line[k * (spaces_between_words + 1) + k + 1:]
            result.append("*" + line + "*")
            i = j

    result.append(border)
    return result

# Example usage
paragraphs = [["bbO","eCStQCgtVDxfKviDfcyZVM","xBbBEdjNhOCVIYPrTClvGzEzTSoi rHEARlSKNUA","htfDNywWZvqYwDFcq","tlkDeVcWRPd GatND","okDXxlRvJwtUyJA","TJAoQZzEJxhPhwDTISYcrBysesEBvrHWP ","PapO
