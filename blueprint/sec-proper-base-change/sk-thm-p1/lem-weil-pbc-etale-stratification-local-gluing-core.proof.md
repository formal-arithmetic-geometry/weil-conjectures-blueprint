+++
kind = "proof"
of = "lem-weil-pbc-etale-stratification-local-gluing-core"
uses = ["def-constructible-stratification"]
+++
Order the affine charts by their indices $1,\dots,n$ and put $V_a=\bigcup_{b<a}W_b$. Each affine open is quasi-compact, and $X$ is quasi-separated, so each $W_b$ is retrocompact and hence constructible; as a finite union, each $V_a$ is open and constructible. Since $W_a$ is a retrocompact open, the image in $X$ of a constructible subset of $W_a$ is constructible (Tag 09YD); in particular the image in $X$ of each local stratum $T_{a,b}$ is constructible. ([def-constructible-stratification]).

Let $C_a$ be the reduced closed subscheme of $X$ with underlying set $X\setminus V_a$. For a local stratum immersion $\iota_{a,b}:Z_{a,b}\to W_a$ put $Z'_{a,b}=Z_{a,b}\times_XC_a$, with the morphism $Z'_{a,b}\to X$ given by the first projection followed by $Z_{a,b}\xrightarrow{\iota_{a,b}}W_a\hookrightarrow X$. The first projection is a base change of the closed immersion $C_a\to X$, hence a closed immersion, so this composite is an immersion. Its image is the image of $Z_{a,b}$ in $X$ intersected with $X\setminus V_a$, a constructible locally closed subset. The first projection $Z'_{a,b}\to Z_{a,b}$ is the required factorization through the local stratum.

Index these pieces by the finitely many pairs $(a,b)$. Pieces with the same $a$ are disjoint, because the local strata of $W_a$ are disjoint and $W_a\to X$ is injective. If $a<a'$, the piece indexed by $a$ lies in $W_a$, whereas the piece indexed by $a'$ avoids $V_{a'}\supseteq W_a$; the other order is symmetric. For coverage, given $x\in X$ choose the least $a$ with $x\in W_a$; then $x\notin V_a$, and $x$ lies in some local stratum $T_{a,b}$, hence in the piece indexed by $(a,b)$. Empty pieces may be retained, as a stratification imposes no nonemptiness requirement. When $n=0$ the covering hypothesis makes $X$ empty and the index set is empty. ([def-constructible-stratification]).

Numbering the pairs $(a,b)$ consecutively, the pieces with their immersions form a stratification $S$ of $X$, with the image, constructibility, local closedness, coverage and disjointness properties just proved. Each stratum immersion factors as $\iota_i=(W_a\hookrightarrow X)\circ\iota_{a,b}\circ q$, where $q$ is the first projection $Z'_{a,b}\to Z_{a,b}$. ([def-constructible-stratification]).
