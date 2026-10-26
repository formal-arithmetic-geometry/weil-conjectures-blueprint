+++
id = "det-def-sfb-shriek-base-change-morphism-compactification"
kind = "lemma"
title = "Base change of a compactification"
order = 2576
uses = ["sk-def-nagata-sketch-data", "sk-def-sfb-dc-setting", "sk-prop-nagata-sketch-comp-category"]
+++
Work in the setting of [sk-def-sfb-dc-setting]. Let
$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
$$
be a cartesian square of the setting and $c=(X\xrightarrow{i}Z\xrightarrow{p}Y)$ a compactification
of $f$ ([sk-def-nagata-sketch-data]). Put $Z':=Z\times_YY'$, with projections $\bar g\colon Z'\to Z$
and $p'\colon Z'\to Y'$, and let $i'\colon X'\to Z'$ be the morphism with $\bar g\circ i'=i\circ g'$
and $p'\circ i'=f'$. Then:

1. $i'$ is well defined, $f'=p'\circ i'$, and both squares
   $$
   \begin{array}{ccc}
   X' & \xrightarrow{\;g'\;} & X\\
   {\scriptstyle i'}\downarrow & & \downarrow{\scriptstyle i}\\
   Z' & \xrightarrow{\;\bar g\;} & Z
   \end{array}
   \qquad\qquad
   \begin{array}{ccc}
   Z' & \xrightarrow{\;\bar g\;} & Z\\
   {\scriptstyle p'}\downarrow & & \downarrow{\scriptstyle p}\\
   Y' & \xrightarrow{\;g\;} & Y
   \end{array}
   $$
   are cartesian;
2. $i'$ is a quasi-compact open immersion and $p'$ is proper, so
   $c':=(X'\xrightarrow{i'}Z'\xrightarrow{p'}Y')$ is a compactification of $f'$, the *base-changed
   compactification* (the base change of compactifications of [sk-prop-nagata-sketch-comp-category]);
3. $Z'$ is separated and of finite type over $k$, and $\bar g,i',p'$ are $k$-morphisms, so both
   squares lie in the setting.
