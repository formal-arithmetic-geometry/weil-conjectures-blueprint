+++
id = "definition-perverse-sheaves-curve"
kind = "definition"
title = "Perverse sheaves on a curve"
order = 1250
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "lemma-perfect-complexes-geometric-point", "definition-punctual-sheaf"]
+++
Let $\Lambda$ be $E$ or $\overline{\mathbf Q}_\ell$. Define two classes of objects of $D^b_c(C_{\mathrm{pro}\acute{e}t},\Lambda)$ by

$$
\begin{split}
{}^pD^{\le0}&=\{K:\mathcal H^aK=0\ (a>0),\
\mathcal H^0K\text{ is punctual}\},\\
{}^pD^{\ge0}&=\{K:\mathcal H^aK=0\ (a<-1),\
\mathcal H^{-1}K\text{ has no nonzero punctual subsheaf}\},
\end{split}
$$

and ${}^pD^{\le n}={}^pD^{\le0}[-n]$, ${}^pD^{\ge n}={}^pD^{\ge0}[-n]$.
A *perverse sheaf* on $C$ is an object of
${}^pD^{\le0}\cap{}^pD^{\ge0}$. For $C=C_0\times_{k_0}k$, a
*perverse Weil sheaf* on $C_0$ is a perverse sheaf on $C$ with a
Weil structure, with morphisms as in Definition [definition-weil-structure].
