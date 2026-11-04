+++
kind = "proof"
of = "proposition-sp-integral-adjunction"
order = 777
uses = ["proposition-sp-unique-adjoint", "lemma-sp-tower-adjunction-foundation"]
+++
We move the adjunction on towers down to $\mathcal O_E$-complexes along the
equivalence of Lemma [lemma-sp-tower-adjunction-foundation]. For this we
need both functors to stay inside normalized towers, which is where the
equivalence holds.

Since $Rf_{!,\bullet}$ and $f^!_\bullet$ preserve normalized towers, the equivalence of
Lemma [lemma-sp-tower-adjunction-foundation] gives
$\operatorname{red}_Y(Rf_{!,\mathcal O_E}M)\simeq Rf_{!,\bullet}\operatorname{red}_XM$ and
$\operatorname{red}_XH_{f,\mathcal O_E}(K)\simeq f^!_\bullet\operatorname{red}_YK$. Using
this lemma and (9.18), we get natural bijections

$$
\begin{aligned}
\Hom(Rf_{!,\mathcal O_E}M,K)
&\simeq\Hom(Rf_{!,\bullet}\operatorname{red}_XM,\operatorname{red}_YK)\\
&\simeq\Hom(\operatorname{red}_XM,f_\bullet^!\operatorname{red}_YK)
\simeq\Hom(M,H_{f,\mathcal O_E}(K)).
\end{aligned}
$$

The second statement follows from Proposition [proposition-sp-unique-adjoint].
