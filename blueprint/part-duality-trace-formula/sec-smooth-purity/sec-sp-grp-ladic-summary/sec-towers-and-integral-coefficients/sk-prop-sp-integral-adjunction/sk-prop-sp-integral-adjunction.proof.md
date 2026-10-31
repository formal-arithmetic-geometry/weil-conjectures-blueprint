+++
kind = "proof"
of = "sk-prop-sp-integral-adjunction"
uses = ["sk-lem-sp-tower", "sk-prop-sp-tower-geometric", "sk-prop-sf-existence"]
+++
Since $Rf_{!,\bullet}$ and $f^!_\bullet$ preserve normalized towers, the equivalence of
Lemma [sk-lem-sp-tower] gives
$\operatorname{red}_Y(Rf_{!,\mathcal O_E}M)\simeq Rf_{!,\bullet}\operatorname{red}_XM$ and
$\operatorname{red}_XH_{f,\mathcal O_E}(K)\simeq f^!_\bullet\operatorname{red}_YK$. Using
this lemma and (10.17), we get natural bijections

$$
\begin{aligned}
\Hom(Rf_{!,\mathcal O_E}M,K)
&\simeq\Hom(Rf_{!,\bullet}\operatorname{red}_XM,\operatorname{red}_YK)\\
&\simeq\Hom(\operatorname{red}_XM,f_\bullet^!\operatorname{red}_YK)
\simeq\Hom(M,H_{f,\mathcal O_E}(K)).
\end{aligned}
$$

The second statement follows from Proposition [sk-prop-sp-unique-adjoint] below.
