x <- "/home/pshy3/share/dataset/RosenfeldC_29_SOL/raw_files_only/cutadapt_trimmed/miRge/miRge.2024-03-12_12-14-08/unmapped.csv"
# x <- gsub("\\", "/", x)
x <- read.csv(x)
summary(x)
x$count <- x$iPSC1_S75_L004_R1 + x$iPSC2_S76_L004_R1 + x$iPSC3_S77_L004_R1 + x$TB1_S72_L004_R1 + x$TB2_S73_L004_R1 + x$TB3_S74_L004_R1

ordered <- x[order(x$count), ]

write.csv(ordered, "../../ordered_sequence.csv")
# Assuming your data frame is named df and your column is named column_name

# Calculate the length of each string in the column
string_lengths <- nchar(x$Sequence)

# Get the count of each length
length_counts <- table(string_lengths)
# Sort length_counts from high to low
sorted_counts <- sort(length_counts, decreasing = TRUE)

# Print the sorted counts
print(sorted_counts)

# Print the counts
print((length_counts))

# Filter rows where the number of characters in column_name is 95
filtered_df <- subset(x, nchar(Sequence) == 95)

# View the filtered dataframe
print(filtered_df$Sequence)

# Count occurrences of each unique string
string_counts <- table(x$Sequence)

# Filter for strings that occur more than once
repeated_strings <- names(string_counts[string_counts > 1])

# View the repeated strings
print(repeated_strings)

library(stringi)

# Assuming your data frame is named df and the column is named column_name
column_data <- x$Sequence

# Concatenate all column values into a single string for more efficient processing
all_text <- paste(column_data, collapse = " ")

# Define a function to find all substrings within the text
find_substrings <- function(s) {
    # This regex attempts to capture substrings of word characters
    pattern <- "(\\w{5,})" # Adjust the {3,} as needed to capture the minimum length of interest

    # Find all matches of the pattern
    matches <- unlist(stri_extract_all_regex(s, pattern))

    # Return the matches
    matches
}

# Find all substrings in the concatenated text
all_substrings <- find_substrings(all_text)

# Count occurrences of each substring
substring_counts <- table(all_substrings)

# Filter for substrings that occur more than 200 times
frequent_substrings <- substring_counts[substring_counts > 5]

# Print the substrings and their counts
print(frequent_substrings)

head(substring_counts)
