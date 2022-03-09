use reqwest;

fn main() {
let mut resp = reqwest::get("https://www.moneycontrol.com/india/stockpricequote/power-generation-distribution/ntpc/NTP")?;
assert!(resp.status().is_success());
}


