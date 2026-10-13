+++
id = "def-sfb-dc-open-base-change-morphism"
kind = "definition"
title = "The extension-by-zero exchange morphism"
order = 1804
uses = ["def-sfb-dc-open-lower-shriek-adjunction", "sk-def-sfb-base-change-morphism"]
+++
Let $\Lambda$ be a commutative condensed ring, and let

$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle j'}\downarrow & & \downarrow{\scriptstyle j}\\
Z' & \xrightarrow{\;g\;} & Z
\end{array}
$$

be a commutative square of the setting with $j$ and $j'$ open immersions. The *extension-by-zero
exchange morphism* $\mathrm{Ex}^{j}_{sq}\colon j'_!\circ Lg'^*\to Lg^*\circ j_!$ on
$D_{\mathrm{cons}}(X,\Lambda)$ is the composite

$$
j'_!Lg'^*\xrightarrow{\ \eta\ }j'_!Lg'^*Lj^*j_!\xrightarrow[\ \sim\ ]{\ \theta\ }j'_!Lj'^*Lg^*j_!\xrightarrow{\ \varepsilon'\ }Lg^*j_!.
$$

Here $\eta$ is the unit of $j_!\dashv Lj^*$ and $\varepsilon'$ the counit of $j'_!\dashv Lj'^*$
([def-sfb-dc-open-lower-shriek-adjunction]). The isomorphism $\theta$ is the pullback
comparison $Lg'^*Lj^*\cong Lj'^*Lg^*$ of [sk-def-sfb-base-change-morphism] for the square
read with $j'$ on top and $g'$, $g$ vertical, whiskered by $j'_!$ on the left and $j_!$ on the right.
