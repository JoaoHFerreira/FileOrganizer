mod yml_parser;
use yml_parser::YmlProcessor;

fn main() {
    let mut processor = YmlProcessor::new("yml_files/configs.yml");
    processor.parse_yml();
    processor.show_current_structure();
}
