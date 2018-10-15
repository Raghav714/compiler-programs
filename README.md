# Left Recursion
# Left Factoring
# Lexical Analyser
# First 
1. For any terminal symbol a, $FIRST({\bf a})$ = $\{{\bf a}\}$.<br />
   Also, $FIRST(\varepsilon)$ = $\{\varepsilon\}$.<br />
2. For any non-terminal $A$ with production rules $A\; \rightarrow\; \alpha_1\; \mid\; \alpha_2\; \mid\; \ldots\; \mid\;<br />    \alpha_n$, $FIRST(A)$ = $FIRST(\alpha_1) \cup FIRST(\alpha_2) \cup \ldots \cup FIRST(\alpha_n)$<br />
3. For any non-terminal $A$ with production rules $A\; \rightarrow\; \alpha_1\; \mid\; \alpha_2\; \mid\; \ldots\; \mid\;<br /> \alpha_n$, $FIRST(A)$ = $FIRST(\alpha_1) \cup FIRST(\alpha_2) \cup \ldots \cup FIRST(\alpha_n)$<br />
For any r.h.s. of the form: $\beta_1 \beta_2 \ldots \beta_n$ (where each $\beta_i$ is a terminal or a non-terminal) we have:<br />
    1. $FIRST(\beta_1)$ is in $FIRST(\beta_1 \beta_2 \ldots \beta_n)$ <br />
       if $\beta_1$ can derive $\varepsilon$, then $FIRST(\beta_2)$ is also in $FIRST(\beta_1 \beta_2 \ldots \beta_n)$<br /> 
       if both $\beta_1$ and $\beta_2$ can derive $\varepsilon$, then $FIRST(\beta_3)$ is also in $FIRST(\beta_1 \beta_2 \ldots \beta_n)$ <br />
       $\cdots$ <br />
    2. if $\beta_1 \beta_2 \ldots \beta_i$ can derive $\varepsilon$, then $FIRST(\beta_{i+1})$ is also in $FIRST(\beta_1 \beta_2 \ldots \beta_n)$<br /> 
       $\varepsilon$ is in $FIRST(\beta_1 \beta_2 \ldots \beta_n)$ only if $\varepsilon$ is in $FIRST(\beta_i)$, for all $0 \leq i \leq n$ 
# Follow
1. If $S$ is the start symbol, then put $\bot$ into $FOLLOW(S)$<br />
2. Examine all rules of the form $A\; \rightarrow\; \alpha X \beta$; then<br />
      1. $FIRST(\beta)$ is in $FOLLOW(X)$<br />
      2. If $\beta$ can derive the empty string then put $FOLLOW(A)$ into $FOLLOW(X)$

# LL1
# Calculator design using lex and yacc
# Other program
