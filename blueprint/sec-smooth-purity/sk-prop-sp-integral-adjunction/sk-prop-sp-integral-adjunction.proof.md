+++
kind = "proof"
of = "sk-prop-sp-integral-adjunction"
uses = ["sk-lem-sp-tower", "sk-prop-sp-tower-geometric", "sk-prop-sf-existence"]
+++
By the tower comparisons and the equivalence
$\operatorname{red}:\Dbc(-,\mathcal O_E)\simeq\Dctf(-_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)_{\mathrm{norm}}$
(inverse $R\varprojlim$, from [sk-lem-sp-tower]),
$\operatorname{red}_Y Rf_{!,\mathcal O_E}M\simeq Rf_{!,\bullet}\operatorname{red}_X M$ and
$\operatorname{red}_X H_{f,\mathcal O_E}(K)\simeq f_\bullet^!\operatorname{red}_Y K$, isomorphisms in
$\Dctf(Y_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$ and
$\Dctf(X_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)$. Hence this equivalence and the
tower adjunction of [sk-prop-sp-tower-geometric] give natural bijections

$$
\begin{aligned}
\operatorname{Hom}(Rf_{!,\mathcal O_E}M,K)
&\simeq\operatorname{Hom}(Rf_{!,\bullet}\operatorname{red}_X M,\operatorname{red}_Y K)\\
&\simeq\operatorname{Hom}(\operatorname{red}_X M,f_\bullet^!\operatorname{red}_Y K)
\simeq\operatorname{Hom}(M,H_{f,\mathcal O_E}(K)).
\end{aligned}
$$

Here the outer Hom groups are taken in $\Dbc(Y,\mathcal O_E)$ and
$\Dbc(X,\mathcal O_E)$, and the middle ones in the tower categories. Uniqueness of
the right adjoint identifies this adjunction with the restriction of
[sk-prop-sf-existence], preserving its unit and counit.

The unit and counit are therefore $R\varprojlim$ of the tower unit and counit,
and their reductions are the finite units and counits. The limit of the tower
purity isomorphism $\gamma_{f,\bullet}$, followed by this identification, gives
the integral purity isomorphism
$\gamma_{f,\mathcal O_E}(K):f_{\mathcal O_E}^{*}K(d)[2d]\xrightarrow{\sim}f_{\mathcal O_E}^!K$
in $\Dbc(X,\mathcal O_E)$ (twisting by the rank-one Tate sheaf and shifting
commute with $R\varprojlim$).
