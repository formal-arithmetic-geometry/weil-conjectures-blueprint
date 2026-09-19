+++
id = "def-open-extension-base-change-mate"
kind = "definition"
title = "Open-extension Beck–Chevalley mate"
order = 56
uses = ["def-derived-pullback", "def-extension-by-zero", "def-weil-finite-coefficient-datum", "prop-extension-by-zero-coefficient-passage", "prop-finite-extension-by-zero-properties"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum], let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, and let
$K\in D^b_c(U,\Lambda)$, with $n\geq1$ in the finite case. For a
Cartesian square with open vertical maps

$$
\begin{CD}
U' @>{g'}>> U\\
@V{j'}VV @VV{j}V\\
X' @>{g}>> X,
\end{CD}
$$

the Cartesian identity gives
$Lg'^*j^*\xrightarrow{\sim}j'^*Lg^*$. Define the mate

$$
\beta_{j,g}(K):j'_!Lg'^*K\longrightarrow Lg^*j_!K
$$

to be adjoint under $j'_!\dashv j'^*$ to

$$
Lg'^*K\xrightarrow{Lg'^*(\eta_j)}Lg'^*j^*j_!K
\xrightarrow{\sim}j'^*Lg^*j_!K,
$$

where $\eta_j:\operatorname{id}\to j^*j_!$ is the inverse of the
restriction isomorphism for extension by zero.
