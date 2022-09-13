num_of_steps = 3

template = f"Report\n\
We have made %count% observations from tossing a coin: \n\
%tails% of them were tails and %heads% of them were heads. \n\
The probabilities are %p_tails%% and %p_heads%%, respectively. \n\
Our forecast is that in the next {num_of_steps} observations we will have: \n\
%new_tails% tail and %new_heads% heads."