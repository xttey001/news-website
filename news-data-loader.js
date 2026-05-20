// 新闻数据加载器 - 按需加载指定日期
const NewsDataLoader = {
	cache: {},
	index: null,
	
	async loadIndex() {
		if (this.index) return this.index;
		const res = await fetch('./news-data-index.json');
		this.index = await res.json();
		return this.index;
	},
	
	async loadDate(date) {
		if (this.cache[date]) return this.cache[date];
		const res = await fetch(`./news-data/${date}.json`);
		const data = await res.json();
		this.cache[date] = data;
		return data;
	},
	
	async getAvailableDates() {
		const index = await this.loadIndex();
		return index.availableDates;
	},
	
	async getLatestDate() {
		const dates = await this.getAvailableDates();
		return dates[0];
	}
};
