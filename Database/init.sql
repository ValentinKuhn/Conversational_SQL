-- users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    date_joined DATE NOT NULL,
    last_login DATE NOT NULL
);

INSERT INTO users (username, email, date_joined, last_login) VALUES
('alice123', 'alice123@email.com', '2023-01-01', '2023-10-27'),
('bob456', 'bob456@email.com', '2023-02-15', '2023-10-25'),
('charlie789', 'charlie789@email.com', '2023-03-10', '2023-10-26'),
('david321', 'david321@email.com', '2023-04-05', '2023-10-24'),
('emma654', 'emma654@email.com', '2023-05-20', '2023-10-28');

-- posts table
CREATE TABLE posts (
    post_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    title VARCHAR NOT NULL,
    content TEXT NOT NULL,
    date_posted DATE NOT NULL
);

INSERT INTO posts (user_id, title, content, date_posted) VALUES
(1, 'Welcome!', 'This is my first post.', '2023-01-05'),
(2, 'My Favorite Foods', 'I love pizza, pasta, and burgers.', '2023-02-20'),
(3, 'Hiking Adventures', 'Last weekend, I went hiking in the mountains. It was beautiful!', '2023-03-15'),
(4, 'Programming Tips', 'Here are some tips for new programmers.', '2023-04-10'),
(5, 'Traveling on a Budget', 'Here are some tips for traveling on a budget.', '2023-05-25');

-- comments table
CREATE TABLE comments (
    comment_id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(post_id),
    user_id INTEGER REFERENCES users(user_id),
    content TEXT NOT NULL,
    date_commented DATE NOT NULL
);

INSERT INTO comments (post_id, user_id, content, date_commented) VALUES
(1, 2, 'Welcome to the blog!', '2023-01-06'),
(2, 1, 'I love pizza too!', '2023-02-21'),
(3, 2, 'That sounds amazing!', '2023-03-16'),
(4, 3, 'Great tips for beginners!', '2023-04-11'),
(5, 4, 'Thanks for the budget tips!', '2023-05-26');
