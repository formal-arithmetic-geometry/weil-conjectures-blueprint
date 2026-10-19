+++
id = "def-nagata-conrad-quasi-domination"
kind = "definition"
title = "Quasi-domination (Conrad)"
lean = ["AlgebraicGeometry.QuasiDomination", "AlgebraicGeometry.QuasiDomination.Extends"]
order = 186
+++
Let $X$ and $Y$ be $S$-schemes with $Y\to S$ separated. A
*quasi-domination of $X$ over $Y$* is a pair $(U,f)$ consisting of a
dense open subscheme $U\subseteq X$ and an $S$-morphism $f\colon U\to Y$
whose graph subscheme

$$
\Gamma_f\hookrightarrow U\times_SY
$$

is closed when viewed as a subscheme of $X\times_SY$. If $U'\subseteq X$ is
an open subscheme and $f'\colon U'\to Y$ an $S$-morphism, a
*quasi-domination of $X$ over $Y$ extending $f'$* is a quasi-domination
$(U,f)$ with $U'\subseteq U\subseteq X$ and $f|_{U'}=f'$.
