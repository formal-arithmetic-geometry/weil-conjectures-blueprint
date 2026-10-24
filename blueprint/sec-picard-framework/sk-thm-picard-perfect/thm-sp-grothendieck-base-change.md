+++
id = "thm-sp-grothendieck-base-change"
kind = "theorem"
title = "Base-change naturality of the Grothendieck spectral sequence"
lean = ["CategoryTheory.Functor.exists_grothendieckSpectralObject_baseChange"]
order = 754
uses = ["def-sp-composite-acyclicity", "def-sp-injective-resolutions", "lem-sp-couple-morphism", "thm-sp-grothendieck", "thm-sp-spectral-object-yields"]
+++
Let $F:\mathcal A\to\mathcal B$, $G:\mathcal B\to\mathcal C$ and
$F':\mathcal A'\to\mathcal B'$, $G':\mathcal B'\to\mathcal C'$ be left exact
additive functors, where $\mathcal A,\mathcal B,\mathcal A',\mathcal B'$ are
Grothendieck abelian and $\mathcal C,\mathcal C'$ are abelian, and let

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
injectives to $G$-acyclics and $F'$ sends injectives to $G'$-acyclics
[def-sp-composite-acyclicity]. Then for $X\in\mathcal A$ there is a morphism
of spectral sequences from the image under $\gamma$ of the Grothendieck
spectral sequence of [thm-sp-grothendieck] for $(F,G)$ at $X$ to the
Grothendieck spectral sequence for $(F',G')$ at $\alpha X$, natural in $X$,
which on $E_2$-terms is the base change morphism

$$
 \gamma\bigl(R^pG(R^qF(X))\bigr)\longrightarrow R^pG'\bigl(R^qF'(\alpha X)\bigr)
$$

assembled from the comparison morphisms $\gamma\circ R^pG\to R^pG'\circ\beta$
and $\beta\circ R^qF\to R^qF'\circ\alpha$ of the right derived functors.
In the base-change situation of the proper-base-change chapter, where
the functors are inverse images along the maps of a cartesian square, this
says that the spectral sequence is compatible with inverse image along a base
change.
