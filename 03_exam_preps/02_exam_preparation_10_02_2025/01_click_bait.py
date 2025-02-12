from collections import deque

suggested_links_score = deque([int(num) for num in input().split()])
featured_articles_popularity = [int(num) for num in input().split()]
target = int(input())
final_feed = []

while suggested_links_score and featured_articles_popularity:
    last_element = featured_articles_popularity.pop()
    first_element = suggested_links_score.popleft()

    if last_element > first_element:
        # LIFO CASE
        dividend = last_element
        divisor = first_element
        remainder = dividend % divisor
        final_feed.append(abs(remainder))
        if remainder != 0:
            remainder *= 2
            featured_articles_popularity.append(remainder)
    elif first_element > last_element:
        # FIFO CASE
        dividend = first_element
        divisor = last_element
        remainder = dividend % divisor
        final_feed.append(-remainder)
        if remainder != 0:
            remainder *= 2
            suggested_links_score.append(remainder)
    else:
        final_feed.append(0)

total_engagement_value = sum(final_feed)

print(f'Final Feed: {", ".join([str(num) for num in final_feed])}')

if total_engagement_value >= target:
    print(f'Goal achieved! Engagement Value: {total_engagement_value}')
else:
    shortfall = target - total_engagement_value
    print(f'Goal not achieved! Short by: {shortfall}')
