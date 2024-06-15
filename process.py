def parse_entry(entry):
    """Parse an entry into its components."""
    parts = entry.strip().split(';')
    if len(parts) != 4:
        raise ValueError("Each entry must have exactly four parts separated by ';'")
    return parts[0], parts[1], parts[2], parts[3]

def format_markdown_entry(author, link, citations, comments):
    """Format a single entry into Markdown on one line."""
    base_sentence = f"- [{author}]({link}) (Citations: {citations})"
    if comments:
        return f"{base_sentence} - {comments}"
    return base_sentence


def process_input_file(input_file):
    """Process the input file and generate Markdown output."""
    with open(input_file, 'r') as file:
        content = file.read().strip()
    entries = content.split('\n')  # Assuming each entry is separated by a blank line
    markdown_output = ""
    for entry in entries:
        author, link, citations, comments = parse_entry(entry)
        markdown_output += format_markdown_entry(author, link, citations, comments) + "\n"
    return markdown_output

print("ML system papers targeting efficient training on heterogeneous cluster(cluster with different types of devices) are less studied than homogeneous cluster(cluster with same type of devices). However, there is a growing interest in this area. The motivation of having heterogeneous cluster in distributed training are:")
print("1. for data centers, the use of heterogeneous GPUs is inevitable due to the short release cycle of new GPU architecture")
print("2. for users, they can purchase spot instance with a combination of available and cheap heterogeneous devices to reduce expense reduce failure's cost(when one type of device failed because of out-biling(bidding price is lower than spot price), the training can still continue on other types of devices).")
print("We have categorized different challenges brought by heterogeneous devices and the corresponding solutions(papers) in the following sections.")
print("If you have any papers to add, feel free to ping me(lukezhuz@umich.edu).")

print("Papers targeting inter-pipeline heterogeneity(each pipeline contains homogeneous devices, different pipelines have heterogeneous devices):")
print("Main problem to solve: inter-pipeline heterogeneity leads to load imbalance if we allocate the same number of mini-batches to each pipeline and update weight when all pipeline ends.")
print("- Papers using batch distribution to balance the workload among pipelines")
input_file = 'inter_pipeline_hetero_batch.txt'  # Change this to the path of your input file
markdown_output = process_input_file(input_file)
print(markdown_output)

print("- Papers using decentralized synchronization to improve overall throughput")
input_file = 'inter_pipeline_hetero_decentralize.txt'  # Change this to the path of your input file
markdown_output = process_input_file(input_file)
print(markdown_output)

print("Papers targeting intra-pipeline heterogeneity(A pipeline contains heterogeneous devices):")
input_file = 'intra_pipeline_hetero.txt'  # Change this to the path of your input file
markdown_output = process_input_file(input_file)
print(markdown_output)

print("Papers targeting communication heterogeneity:")
input_file = 'communication_hetero.txt'  # Change this to the path of your input file
markdown_output = process_input_file(input_file)
print(markdown_output)

print("Other papers targeting heterogeneous cluster(I haven't dived into):")
input_file = 'others.txt'
markdown_output = process_input_file(input_file)
print(markdown_output)
