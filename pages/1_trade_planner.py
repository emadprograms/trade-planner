import streamlit as st
import pandas as pd

# Set the page configuration to use the wide layout
st.set_page_config(layout="wide")

def trading_plan_form():
    """
    Creates a Streamlit form for an intraday trading plan, incorporating market narrative.
    """
    st.header("Intraday Trading Plan")

    # I. Pre-Market Analysis
    with st.expander("I. Pre-Market Analysis"):
        st.subheader("I. Pre-Market Analysis")

        # First Row: Stock, Premarket Price, Day's Expected Range
        col1, col2, col3 = st.columns(3)
        with col1:
            stock = st.text_input("Stock", placeholder="e.g., AAPL", key="stock")
        with col2:
            premarket_price = st.number_input("Premarket Price", format="%.2f", key="premarket_price")
        with col3:
            day_expected_range = st.text_input("Day's Expected Range", placeholder="e.g., High/Low estimate", key="day_expected_range")

        # Second Row: Average Volume, Short Interest, Short Ratio
        col4, col5, col6 = st.columns(3)
        with col4:
            average_volume = st.number_input("Average Volume (in millions)", format="%.2f", key="average_volume")
        with col5:
            short_interest = st.number_input("Short Interest", format="%.2f", key="short_interest")
        with col6:
            short_ratio = st.number_input("Short Ratio (Days to Cover)", format="%.2f", key="short_ratio")

        market_context = st.text_area("Market Context", placeholder="Briefly describe the overall market conditions...", key="market_context")
        overall_bias = st.selectbox("Overall Bias", ["Bullish", "Bearish", "Neutral"], key="overall_bias")
        key_catalysts = st.text_area("Key Catalysts", placeholder="List any news, earnings, or economic data...", key="key_catalysts")
        sector = st.text_input("Sector", placeholder="e.g., Technology", key="sector")
        sector_news = st.text_area("Sector News", placeholder="Summarize any relevant news or trends...", key="sector_news")

        st.subheader("Pre-market Checklist")
        check_news = st.checkbox("Check for news and earnings releases", key="check_news")
        review_overnight = st.checkbox("Review overnight price action and volume", key="review_overnight")
        identify_gaps = st.checkbox("Identify potential gaps and their implications", key="identify_gaps")
        analyze_volume = st.checkbox("Analyze pre-market volume and relative strength", key="analyze_volume_checkbox")
        initial_narrative_assessment = st.text_area("Initial Market Narrative Assessment", placeholder="Note any early observations about market sentiment...", key="initial_narrative_assessment")

    # II. Key Levels
    with st.expander("II. Key Levels"):
        st.subheader("II. Key Levels")
        st.subheader("Market-Recognized Levels (Previous Day/Week/Month)")
        resistance_2 = st.number_input("Resistance 2", format="%.2f", key="resistance_2")
        resistance_1 = st.number_input("Resistance 1", format="%.2f", key="resistance_1")
        pivot_point = st.number_input("Pivot Point", format="%.2f", key="pivot_point")
        support_1 = st.number_input("Support 1", format="%.2f", key="support_1")
        support_2 = st.number_input("Support 2", format="%.2f", key="support_2")
        previous_day_close = st.number_input("Previous Day Close", format="%.2f", key="previous_day_close")

        st.subheader("Intraday Levels (1-Minute Chart)")
        intraday_resistance = st.text_area("Intraday Resistance", placeholder="Price(s) where price sharply reversed downwards...", key="intraday_resistance")
        intraday_support = st.text_area("Intraday Support", placeholder="Price(s) where price sharply reversed upwards...", key="intraday_support")
        current_price = st.number_input("Current Price", format="%.2f", key="current_price")
        level_confluences = st.checkbox("Note any areas where Market-Recognized Levels and Intraday Levels align...", key="level_confluences")

    # III. Primary Trade Setup
    with st.expander("III. Primary Trade Setup"):
        st.subheader("III. Primary Trade Setup")
        level_of_interest = st.text_input("Level of Interest", placeholder="e.g., 123-123.5 range", key="level_of_interest")
        trade_direction = st.selectbox("Trade Direction", ["Long", "Short"], key="trade_direction")
        entry_condition = st.text_area("Entry Condition", placeholder="Specific price action, e.g., price reaches top of range...", key="entry_condition")
        target = st.text_input("Target", placeholder="e.g., 120", key="target")
        stop_loss = st.text_input("Stop-Loss", placeholder="e.g., Above 124", key="stop_loss")
        initial_position_size = st.text_input("Initial Position Size", placeholder="To be calculated based on risk and capital", key="initial_position_size")

        st.subheader("Entry Timing")
        consider_time = st.checkbox("Consider the time of day and its typical volatility.", key="consider_time")
        note_specific_times = st.text_area("Note any specific times to avoid or favor trading.", placeholder="e.g., Avoid trading in the first 15 minutes...", key="note_specific_times")

        st.subheader("Trade Confluences")
        list_additional_factors = st.text_area("List any additional factors that support the trade setup", placeholder="e.g., trend alignment, chart patterns...", key="list_additional_factors")
        narrative_context = st.text_area("Narrative Context", placeholder="Describe the prevailing market narrative...", key="narrative_context")

    # IV. What Ifs (Reactive Scenarios)
    with st.expander("IV. What Ifs (Reactive Scenarios)"):
        st.subheader("IV. What Ifs (Reactive Scenarios)")

        st.subheader("A. Pre-Market Scenarios")
        st.markdown("1. What if the stock breaks a key level in the pre-market?")
        if_premarket_break_condition = st.text_area("IF", placeholder="e.g., Price breaks above Resistance 1...", key="if_premarket_break")
        then_premarket_break_action = st.text_area("THEN", placeholder="e.g., Adjust entry strategy...", key="then_premarket_break")

        st.markdown("2. What if the opening price is far from my Level of Interest?")
        if_opening_price_far_condition = st.text_area("IF", placeholder="e.g., The opening price is more than 1% away...", key="if_opening_price_far")
        then_opening_price_far_action = st.text_area("THEN", placeholder="e.g., Re-evaluate the relevance of the level...", key="then_opening_price_far")

        st.subheader("B. Opening Bell Scenarios")
        st.markdown("3. What if the stock has a large overnight gap?")
        if_overnight_gap_condition = st.text_area("IF", placeholder="e.g., Stock gaps up or down significantly (>2%)...", key="if_overnight_gap")
        then_overnight_gap_action = st.text_area("THEN", placeholder="e.g., Wait for the first 30 minutes of trading...", key="then_overnight_gap")

        st.markdown("4. What if the stock reverses sharply at the open?")
        if_sharp_reversal_condition = st.text_area("IF", placeholder="e.g., Stock opens near a key level, then reverses...", key="if_sharp_reversal")
        then_sharp_reversal_action = st.text_area("THEN", placeholder="e.g., Consider trading the reversal...", key="then_sharp_reversal")
        narrative_reversal = st.text_area("Narrative Consideration", placeholder="Note the initial market narrative and how it aligns...", key="narrative_reversal")

        st.subheader("C. During the Trading Day Scenarios (Before Level of Interest)")
        st.markdown("5. What if price reverses before reaching the Level of Interest?")
        if_reversal_before_condition = st.text_area("IF", placeholder="e.g., Price shows strong bullish momentum before 123...", key="if_reversal_before")
        then_reversal_before_action = st.text_area("THEN", placeholder="e.g., Re-evaluate bias...", key="then_reversal_before")
        narrative_reversal_before = st.text_area("Narrative Consideration", placeholder="Is this reversal supported by the prevailing narrative?...", key="narrative_reversal_before")

        st.markdown("6. What if the stock is strongly trending?")
        if_strong_trend_condition = st.text_area("IF", placeholder="e.g., The stock is in a strong uptrend...", key="if_strong_trend")
        then_strong_trend_action = st.text_area("THEN", placeholder="e.g., Favor long trades...", key="then_strong_trend")
        narrative_strong_trend = st.text_area("Narrative Consideration", placeholder="Ensure the narrative supports continued trend strength...", key="narrative_strong_trend")

        st.markdown("7. What if the stock is range-bound?")
        if_range_bound_condition = st.text_area("IF", placeholder="e.g., The stock is trading in a defined range...", key="if_range_bound")
        then_range_bound_action = st.text_area("THEN", placeholder="e.g., Buy near support, sell near resistance...", key="then_range_bound")
        narrative_range_bound = st.text_area("Narrative Consideration", placeholder="Is the range-bound behavior due to conflicting narratives?...", key="narrative_range_bound")

        st.subheader("D. At the Level of Interest")
        st.markdown("8. What if price blows through the Level of Interest?")
        if_blow_through_condition = st.text_area("IF", placeholder="e.g., Price breaks above 123.5...", key="if_blow_through")
        then_blow_through_action = st.text_area("THEN", placeholder="e.g., Invalidate short setup...", key="then_blow_through")
        narrative_blow_through = st.text_area("Narrative Consideration", placeholder="Does this breakout confirm the prevailing narrative?...", key="narrative_blow_through")

        st.markdown("9. What if price consolidates at the Level of Interest?")
        if_consolidates_condition = st.text_area("IF", placeholder="e.g., Price consolidates in the 123-123.5 range...", key="if_consolidates")
        then_consolidates_action = st.text_area("THEN", placeholder="e.g., Be cautious. Reduce position size...", key="then_consolidates")
        narrative_consolidates = st.text_area("Narrative Consideration", placeholder="Is this consolidation a sign of narrative indecision?...", key="narrative_consolidates")

        st.markdown("10. What if the stock's trading volume is low at a key level?")
        if_low_volume_condition = st.text_area("IF", placeholder="e.g., Price approaches a key level...", key="if_low_volume")
        then_low_volume_action = st.text_area("THEN", placeholder="e.g., Reduce position size...", key="then_low_volume")
        narrative_low_volume = st.text_area("Narrative Consideration", placeholder="Does the low volume suggest a lack of conviction?...", key="narrative_low_volume")

        st.markdown("11. What if the stock shows a false breakout?")
        if_false_breakout_condition = st.text_area("IF", placeholder="e.g., Price breaks a key resistance level...", key="if_false_breakout")
        then_false_breakout_action = st.text_area("THEN", placeholder="e.g., Be cautious on longs...", key="then_false_breakout")
        narrative_false_breakout = st.text_area("Narrative Consideration", placeholder="Does this false breakout signal a potential narrative change?...", key="narrative_false_breakout")

        st.subheader("E. After Target is Reached")
        st.markdown("12. What if the target is reached quickly?")
        if_target_reached_quickly_condition = st.text_area("IF", placeholder="e.g., Price reaches 120 very quickly...", key="if_target_reached_quickly")
        then_target_reached_quickly_action = st.text_area("THEN", placeholder="e.g., Scale out some profits...", key="then_target_reached_quickly")
        narrative_target_reached_quickly = st.text_area("Narrative Consideration", placeholder="Does the strength of the move suggest the narrative is likely to continue?...", key="narrative_target_reached_quickly")

        st.subheader("F. Other Scenarios")
        st.markdown("13. What if the stock's volatility increases significantly?")
        if_volatility_increase_condition = st.text_area("IF", placeholder="e.g., The stock's ATR increases significantly...", key="if_volatility_increase")
        then_volatility_increase_action = st.text_area("THEN", placeholder="e.g., Reduce position size...", key="then_volatility_increase")
        narrative_volatility_increase = st.text_area("Narrative Consideration", placeholder="Is the increased volatility a sign of a narrative shift?...", key="narrative_volatility_increase")

        st.markdown("14. What if the stock fails to hold an important level?")
        if_fails_hold_level_condition = st.text_area("IF", placeholder="e.g., Price breaks a key support level...", key="if_fails_hold_level")
        then_fails_hold_level_action = st.text_area("THEN", placeholder="e.g., Close long position...", key="then_fails_hold_level")
        narrative_fails_hold_level = st.text_area("Narrative Consideration", placeholder="Does this failure confirm a bearish narrative?...", key="narrative_fails_hold_level")

        st.markdown("15. What if the stock gaps and then consolidates?")
        if_gaps_consolidates_condition = st.text_area("IF", placeholder="e.g., Stock gaps up or down and then consolidates...", key="if_gaps_consolidates")
        then_gaps_consolidates_action = st.text_area("THEN", placeholder="e.g., Wait for a breakout from the consolidation...", key="then_gaps_consolidates")
        narrative_gaps_consolidates = st.text_area("Narrative Consideration", placeholder="What does the consolidation tell us about the strength of the gap narrative?...", key="narrative_gaps_consolidates")

        st.markdown("16. What if the stock is halted multiple times?")
        if_stock_halted_condition = st.text_area("IF", placeholder="e.g., Stock is halted multiple times...", key="if_stock_halted")
        then_stock_halted_action = st.text_area("THEN", placeholder="e.g., Greatly reduce or eliminate position...", key="then_stock_halted")
        narrative_stock_halted = st.text_area("Narrative Consideration", placeholder="Halts indicate high uncertainty and a potentially unstable narrative...", key="narrative_stock_halted")

        st.markdown("17. What if the stock is approaching a major news event?")
        if_news_event_condition = st.text_area("IF", placeholder="e.g., Stock approaching earnings release...", key="if_news_event")
        then_news_event_action = st.text_area("THEN", placeholder="e.g., Reduce position size significantly...", key="then_news_event")
        narrative_news_event = st.text_area("Narrative Consideration", placeholder="The news event will likely create a new narrative...", key="narrative_news_event")

    # V. Risk Management
    with st.expander("V. Risk Management"):
        st.subheader("V. Risk Management")
        position_sizing = st.text_input("Position Sizing", placeholder="e.g., Calculate in real-time...", key="position_sizing")
        max_daily_loss = st.number_input("Maximum Daily Loss", placeholder="e.g., State the maximum amount you are willing to lose...", format="%.2f", key="max_daily_loss")
        contingency_plan = st.text_area("Contingency Plan", placeholder="Describe your plan if your maximum daily loss is hit...", key="contingency_plan")

        st.subheader("Risk Assessment Checklist")
        check_position_size = st.checkbox("Confirm position size aligns with risk tolerance.", key="check_position_size")
        ensure_stop_loss = st.checkbox("Ensure stop-loss is appropriately placed.", key="ensure_stop_loss")
        evaluate_risk_reward = st.checkbox("Evaluate the risk/reward ratio of the trade.", key="evaluate_risk_reward")
        consider_correlated_trades = st.checkbox("Consider the impact of correlated trades.", key="consider_correlated_trades")
        narrative_risk_assessment = st.text_area("Narrative Risk Assessment", placeholder="How might the evolving market narrative affect the risk of this trade?...", key="narrative_risk_assessment")

    # VI. Trade Management
    with st.expander("VI. Trade Management"):
        st.subheader("VI. Trade Management")
        scaling_in_out = st.text_area("Scaling In/Out", placeholder="Describe if and how you will scale into or out of positions...", key="scaling_in_out")
        time_management = st.text_area("Time Management", placeholder="Note any time-based rules...", key="time_management")
        notes = st.text_area("Notes", placeholder="Use this section for any additional notes or observations...", key="notes")
        post_trade_review = st.text_area("Post-Trade Review", placeholder="Describe how you will review your trades...", key="post_trade_review")

        st.subheader("Trade Review Questions")
        check_entry_plan = st.checkbox("Was the entry in line with the trading plan?", key="check_entry_plan")
        check_stop_loss = st.checkbox("Was the stop-loss correctly placed and honored?", key="check_stop_loss")
        check_target = st.checkbox("Was the target achieved? If not, why?", key="check_target")
        check_emotions = st.checkbox("Were emotions controlled throughout the trade?", key="check_emotions")
        check_lessons = st.checkbox("What lessons can be learned from this trade?", key="check_lessons")
        narrative_review = st.text_area("Narrative Review", placeholder="How did the market narrative evolve during the trade?...", key="narrative_review")

    # Create a dictionary to store the data
    data = {
        "Stock": stock,
        "Premarket Price": premarket_price,
        "Day's Expected Range": day_expected_range,
        "Market Context": market_context,
        "Overall Bias": overall_bias,
        "Key Catalysts": key_catalysts,
        "Sector": sector,
        "Sector News": sector_news,
        "Average Volume": average_volume,
        "Short Interest": short_interest,
        "Short Ratio (Days to Cover)": short_ratio,

        "Check for news and earnings releases": check_news,
        "Review overnight price action and volume": review_overnight,
        "Identify potential gaps and their implications": identify_gaps,
        "Analyze pre-market volume and relative strength": analyze_volume,
        "Initial Market Narrative Assessment": initial_narrative_assessment,

        "Resistance 2": resistance_2,
        "Resistance 1": resistance_1,
        "Pivot Point": pivot_point,
        "Support 1": support_1,
        "Support 2": support_2,
        "Previous Day Close": previous_day_close,

        "Intraday Resistance": intraday_resistance,
        "Intraday Support": intraday_support,
        "Current Price": current_price,
        "Level Confluences": level_confluences,

        "Level of Interest": level_of_interest,
        "Trade Direction": trade_direction,
        "Entry Condition": entry_condition,
        "Target": target,
        "Stop-Loss": stop_loss,
        "Initial Position Size": initial_position_size,

        "Consider the time of day and its typical volatility.": consider_time,
        "Note any specific times to avoid or favor trading.": note_specific_times,

        "List any additional factors that support the trade setup": list_additional_factors,
        "Narrative Context": narrative_context,

        "IF - Premarket Break": if_premarket_break_condition,
        "THEN - Premarket Break": then_premarket_break_action,
        "IF - Opening Price Far": if_opening_price_far_condition,
        "THEN - Opening Price Far": then_opening_price_far_action,

        "IF - Overnight Gap": if_overnight_gap_condition,
        "THEN - Overnight Gap": then_overnight_gap_action,
        "IF - Sharp Reversal": if_sharp_reversal_condition,
        "THEN - Sharp Reversal": then_sharp_reversal_action,
        "Narrative Consideration - Sharp Reversal": narrative_reversal,

        "IF - Reversal Before": if_reversal_before_condition,
        "THEN - Reversal Before": then_reversal_before_action,
        "Narrative Consideration - Reversal Before": narrative_reversal_before,

        "IF - Strong Trend": if_strong_trend_condition,
        "THEN - Strong Trend": then_strong_trend_action,
        "Narrative Consideration - Strong Trend": narrative_strong_trend,

        "IF - Range Bound": if_range_bound_condition,
        "THEN - Range Bound": then_range_bound_action,
        "Narrative Consideration - Range Bound": narrative_range_bound,

        "IF - Blow Through": if_blow_through_condition,
        "THEN - Blow Through": then_blow_through_action,
        "Narrative Consideration - Blow Through": narrative_blow_through,

        "IF - Consolidates": if_consolidates_condition,
        "THEN - Consolidates": then_consolidates_action,
        "Narrative Consideration - Consolidates": narrative_consolidates,

        "IF - Low Volume": if_low_volume_condition,
        "THEN - Low Volume": then_low_volume_action,
        "Narrative Consideration - Low Volume": narrative_low_volume,

        "IF - False Breakout": if_false_breakout_condition,
        "THEN - False Breakout": then_false_breakout_action,
        "Narrative Consideration - False Breakout": narrative_false_breakout,

        "IF - Target Reached Quickly": if_target_reached_quickly_condition,
        "THEN - Target Reached Quickly": then_target_reached_quickly_action,
        "Narrative Consideration - Target Reached Quickly": narrative_target_reached_quickly,

        "IF - Volatility Increase": if_volatility_increase_condition,
        "THEN - Volatility Increase": then_volatility_increase_action,
        "Narrative Consideration - Volatility Increase": narrative_volatility_increase,

        "IF - Fails Hold Level": if_fails_hold_level_condition,
        "THEN - Fails Hold Level": then_fails_hold_level_action,
        "Narrative Consideration - Fails Hold Level": narrative_fails_hold_level,

        "IF - Gaps Consolidates": if_gaps_consolidates_condition,
        "THEN - Gaps Consolidates": then_gaps_consolidates_action,
        "Narrative Consideration - Gaps Consolidates": narrative_gaps_consolidates,

        "IF - Stock Halted": if_stock_halted_condition,
        "THEN - Stock Halted": then_stock_halted_action,
        "Narrative Consideration - Stock Halted": narrative_stock_halted,

        "IF - News Event": if_news_event_condition,
        "THEN - News Event": then_news_event_action,
        "Narrative Consideration - News Event": narrative_news_event,

        "Position Sizing": position_sizing,
        "Maximum Daily Loss": max_daily_loss,
        "Contingency Plan": contingency_plan,

        "Confirm position size aligns with risk tolerance.": check_position_size,
        "Ensure stop-loss is appropriately placed.": ensure_stop_loss,
        "Evaluate the risk/reward ratio of the trade.": evaluate_risk_reward,
        "Consider the impact of correlated trades.": consider_correlated_trades,
        "Narrative Risk Assessment": narrative_risk_assessment,

        "Scaling In/Out": scaling_in_out,
        "Time Management": time_management,
        "Notes": notes,
        "Post-Trade Review": post_trade_review,

        "Was the entry in line with the trading plan?": check_entry_plan,
        "Was the stop-loss correctly placed and honored?": check_stop_loss,
        "Was the target achieved? If not, why?": check_target,
        "Were emotions controlled throughout the trade?": check_emotions,
        "What lessons can be learned from this trade?": check_lessons,
        "Narrative Review": narrative_review,
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame([data])

    # Save the data to a CSV file
    if st.button("Save Trading Plan"):
        df.to_csv("trading_plan.csv", index=False)
        st.success("Trading plan saved to trading_plan.csv")

if __name__ == "__main__":
    trading_plan_form()