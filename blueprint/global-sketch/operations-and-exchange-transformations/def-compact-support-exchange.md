+++
id = "def-compact-support-exchange"
kind = "definition"
title = "Compact-support exchange transformation"
order = 59
uses = ["def-all-coefficient-compact-support", "def-compactification-category", "def-derived-direct-image", "def-derived-pullback", "def-direct-image-exchange", "def-open-extension-exchange", "def-qbar-ambient-derived-category", "def-weil-finite-coefficient-datum", "prop-extension-by-zero-coefficient-passage"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum], and let
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case. In the Cartesian square of
Definition [def-direct-image-exchange], choose
a compactification $f=p\circ j$,

$$
X\xrightarrow{j}\overline X\xrightarrow{p}Y,
$$

and pull it back to
$X'\xrightarrow{j'}\overline X'\xrightarrow{p'}Y'$, with
$\bar g:\overline X'\to\overline X$. For
$K\in D^b_c(X,\Lambda)$, where $\Lambda$ denotes one of the explicitly
constructed coefficient levels, define

$$
\operatorname{Ex}_!(K):Lg^*Rf_!K\longrightarrow Rf'_!Lg'^*K
$$

to be the following displayed composite in the ambient category

$$
\begin{cases}
D\bigl(Y'_{\mathrm{proet}},
(\mathcal O_E/\varpi_E^n)_{Y'}\bigr),
&\Lambda=\mathcal O_E/\varpi_E^n,\\
D\bigl(Y'_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y'}\bigr),
&\Lambda=\mathcal O_E,\\
D(Y'_{\mathrm{proet}},E_{Y'}),&\Lambda=E,\\
D(Y',\Qlb),&\Lambda=\Qlb,
\end{cases}
$$

where the last category is the ambient category of
Definition [def-qbar-ambient-derived-category]:

$$
\begin{aligned}
Lg^*Rf_!K
&\xrightarrow{\sim} Lg^*Rp_*j_!K\\
&\xrightarrow{\operatorname{Ex}_*(j_!K)}
Rp'_*L\bar g^*j_!K\\
&\xrightarrow{Rp'_*(\operatorname{Ex}_{j,\bar g}(K))}
Rp'_*j'_!Lg'^*K
\xrightarrow{\sim}Rf'_!Lg'^*K.
\end{aligned}
$$

The middle first arrow is the direct-image exchange $\operatorname{Ex}_*$
for the proper map $p$, and the middle second arrow is the open-extension
exchange of Definition [def-open-extension-exchange]. At finite level,
the first and last arrows are the defining compactification identifications.
At the integral, rational, and $\Qlb$ levels they are induced from those
finite identifications by coefficient passage for extension by zero and by
the all-coefficient compact-support construction. Constructible
landing, invertibility, independence of the chosen compactification,
pasting, and coefficient compatibility are asserted only in
Proposition [prop-compact-support-base-change].
