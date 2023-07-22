-- SQL Schema for Storing Posts

-- If a table called posts already exists, drop it
drop table if exists posts;
	create table posts (
		id integer primary key autoincrement,	-- unique ID
		name text not null,		-- post has creator name
		content text not null,	-- post has content
		time text not null		-- post has time
);
		
