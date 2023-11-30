use std::fs;
use std::collections::HashMap;

pub struct YmlProcessor {
    yml_contents: String,
    hash_map: HashMap<String, String>,
}

impl YmlProcessor {
    pub fn new(file_path: &str) -> Self {
        let contents = fs::read_to_string(file_path)
            .expect("Should have been able to read the file");
        Self {
            yml_contents: contents,
            hash_map: HashMap::new(),
        }
    }

    pub fn parse_yml(&mut self) {
        let topics = self.get_folders_vec();
        self.get_yml_hash_map_structure(topics);
    }

    fn get_folders_vec(&self) -> Vec<Vec<String>> {
        self.yml_contents.split('\n')
            .map(|line| line.split_whitespace().filter(|s| !s.is_empty()).map(|s| s.to_string()).collect())
            .filter(|v: &Vec<String>| v.len() > 1)
            .collect()
    }

    fn get_yml_hash_map_structure(&mut self, topics: Vec<Vec<String>>) {
        let mut hash_map = HashMap::new();
        for topic in topics {
            match topic.as_slice()  {
                [key, value] => { hash_map.insert(key.clone(), value.clone()); },
                _ => continue,
            }
        }
        self.hash_map = hash_map;
    }

    pub fn show_current_structure(&self) {
        for (key, value) in &self.hash_map {
            println!("{}: {}", key, value);
        }
    }
}