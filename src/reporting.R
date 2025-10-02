library(ggplot2)

# Load data
# Using check.names=FALSE to prevent R from automatically changing column names
data <- read.csv('data/bank_transactions.csv', check.names=FALSE)

# Create a transaction_amount column using the EXACT column names from the file
# We use backticks (`) to handle the spaces and special characters.
data$transaction_amount <- data$` WITHDRAWAL AMT ` - data$` DEPOSIT AMT `

# Generate a risk report plot using the uppercase 'DATE' column
# The y-axis uses the new column we just created.
ggplot(data, aes(x=DATE, y=transaction_amount)) +
    geom_line() +
    labs(title="Transaction Amount Over Time (Static R Report)", x="Date", y="Transaction Amount") +
    theme_minimal()

# Save the plot
ggsave("risk_report.png", width = 10, height = 6)

print("Generated and saved risk_report.png successfully.")