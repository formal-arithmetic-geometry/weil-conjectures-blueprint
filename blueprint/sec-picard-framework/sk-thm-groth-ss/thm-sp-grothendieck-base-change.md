+++
id = "thm-sp-grothendieck-base-change"
kind = "theorem"
title = "Base-change naturality of the Grothendieck spectral sequence"
order = 610
uses = ["def-sp-composite-acyclicity", "def-sp-injective-resolutions", "lem-sp-couple-morphism", "thm-sp-grothendieck", "thm-sp-spectral-object-yields"]
+++
Let $(F,G)$ and $(F',G')$ be composable pairs
[def-sp-composite-acyclicity] in Grothendieck abelian categories $\mathcal
A,\mathcal B,\mathcal C$ and $\mathcal A',\mathcal B',\mathcal C'$, and let

$$
 \alpha:\mathcal A\to\mathcal A',\qquad
 \beta:\mathcal B\to\mathcal B',\qquad
 \gamma:\mathcal C\to\mathcal C'
$$

be additive *exact* functors making the squares

$$
\begin{array}{ccc}
\mathcal A&\xrightarrow{F}&\mathcal B\\
\downarrow\alpha&&\downarrow\beta\\
\mathcal A'&\xrightarrow{F'}&\mathcal B'
\end{array}
\qquad
\begin{array}{ccc}
\mathcal B&\xrightarrow{G}&\mathcal C\\
\downarrow\beta&&\downarrow\gamma\\
\mathcal B'&\xrightarrow{G'}&\mathcal C'
\end{array}
$$

commute up to fixed natural isomorphisms, and suppose that $F$ sends
injectives to $G$-acyclics and $F'$ sends injectives to $G'$-acyclics. Then
the Grothendieck spectral sequences of [thm-sp-grothendieck] for $(F,G)$ and
$(F',G')$ are related by a morphism of spectral sequences natural in all the
data. In the base-change situation of the proper-base-change chapter, where
the functors are inverse images along the maps of a cartesian square, this
says that the spectral sequence is compatible with inverse image along a base
change.
