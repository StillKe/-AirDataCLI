import cmd
import shlex
import sys

class AirbnbDataTool(cmd.Cmd):
    """Command-line tool for managing data pipelines and analytics at Airbnb."""

    prompt = 'airbnb> '

    def do_start_pipeline(self, pipeline_name):
        """Start a data pipeline."""
        print(f"Starting pipeline: {pipeline_name}")

    def do_stop_pipeline(self, pipeline_name):
        """Stop a data pipeline."""
        print(f"Stopping pipeline: {pipeline_name}")

    def do_monitor_pipeline(self, pipeline_name):
        """Monitor the status of a data pipeline."""
        print(f"Monitoring pipeline: {pipeline_name}")

    def do_clean_data(self, dataset_name):
        """Clean and preprocess the specified dataset."""
        print(f"Cleaning data for dataset: {dataset_name}")

    def do_run_analytics(self, dataset_name):
        """Run analytics on the specified dataset."""
        print(f"Running analytics on dataset: {dataset_name}")

    def do_generate_report(self, report_name):
        """Generate a report based on the analytics."""
        print(f"Generating report: {report_name}")

    def do_quit(self, line):
        """Exit the tool."""
        print("Quitting...")
        return True

    def do_help(self, line):
        """Display help information for commands."""
        if line:
            cmd.Cmd.do_help(self, line)
        else:
            print("Available commands:")
            print("  start_pipeline [pipeline_name] - Start a data pipeline")
            print("  stop_pipeline [pipeline_name] - Stop a data pipeline")
            print("  monitor_pipeline [pipeline_name] - Monitor the status of a data pipeline")
            print("  clean_data [dataset_name] - Clean and preprocess the specified dataset")
            print("  run_analytics [dataset_name] - Run analytics on the specified dataset")
            print("  generate_report [report_name] - Generate a report based on the analytics")
            print("  quit - Exit the tool")
            print("  help - Display this help information")

    def default(self, line):
        """Handle unrecognized commands."""
        print(f"Unrecognized command: {line}")
        self.do_help(line)

if __name__ == '__main__':
    try:
        AirbnbDataTool().cmdloop()
    except KeyboardInterrupt:
        print("\nQuitting...")
        sys.exit(0)