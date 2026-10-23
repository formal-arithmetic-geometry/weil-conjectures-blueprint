+++
kind = "proof"
of = "lem-wf-lisse-stalk-vanishing"
uses = ["def-weil-pbc-proetale-site", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-qlbar-condensed", "det-def-sfb-module-pushforward-pullback", "sk-prop-pe-condensed-point"]
+++
(1) Write $\Lambda=\underline{\Qlb}$. Choose a pro-étale cover $\{f_i:V_i\to X\}$
([def-weil-pbc-proetale-site]) with isomorphisms
$f_i^*H\simeq\Lambda_{V_i}^{\oplus n_i}$. Fix $i$ with $V_i\neq\emptyset$, a point $v\in V_i$,
and put $x=f_i(v)$; by hypothesis there is a geometric point $s:\Spec K\to X$ over $x$ with
$H_s=0$.

*$s$ lifts to $V_i$.* The fibre product $W=V_i\times_X\Spec K$ is nonempty: its points over
$(v,\Spec K)$ correspond to the primes of $\kappa(v)\otimes_{\kappa(x)}K$
([Tag 01JT](https://stacks.math.columbia.edu/tag/01JT)), a nonzero ring, being a tensor product
of two nonzero vector spaces over the field $\kappa(x)$. The projection $W\to\Spec K$ is weakly
étale, as a base change of $f_i$. Let $W'\subseteq W$ be a nonempty affine open. Since $K$ is
separably closed, the affine pro-étale objects over $\Spec K$ are the profinite sets
([sk-prop-pe-condensed-point]); $W'$ corresponds to a nonempty profinite set, and its map to
the one-point set has a section $\Spec K\to W'$. Composing with $W'\subseteq W\to V_i$ gives
$t:\Spec K\to V_i$ with $f_i\circ t=s$.

*The stalk.* By the composition isomorphism of pullbacks
([det-def-sfb-module-pushforward-pullback]) and $t^*\Lambda_{V_i}\simeq\Lambda_{\Spec K}$
([det-def-sfb-pulled-back-coefficients]),

$$
s^*H\simeq t^*f_i^*H\simeq t^*\Lambda_{V_i}^{\oplus n_i}\simeq\Lambda_{\Spec K}^{\oplus n_i},
\qquad\text{so}\qquad
0=H_s\simeq\Gamma(\Spec K,\Lambda_{\Spec K})^{\oplus n_i}=\Qlb^{\oplus n_i},
$$

the sections of $\underline{\Qlb}$ over the point being the constant functions, i.e. $\Qlb$
([det-def-sfb-qlbar-condensed], [sk-prop-pe-condensed-point]). Hence $n_i=0$ and
$f_i^*H=0$; for $V_i=\emptyset$ this holds trivially.

*Conclusion.* For an object $V_i$ of $X_{\mathrm{proét}}$ the pullback $f_i^*H$ is the
restriction of $H$ to $V_i$. So $H(U')=0$ for every object $U'$ lying over some $V_i$, and for
an arbitrary object $U$ the sheaf axiom for the cover $\{U\times_XV_i\to U\}$ presents $H(U)$
as a subgroup of $\prod_iH(U\times_XV_i)=0$. Hence $H=0$.

(2) Let $z\in Z$ and let $t:\Spec K\to Z$ be a geometric point over $z$. By the composition
isomorphism of pullbacks, $(g^*H)_t=\Gamma(\Spec K,t^*g^*H)\simeq\Gamma(\Spec K,(g\circ t)^*H)
=H_{g\circ t}=0$. So the lisse module $g^*H$ satisfies the hypothesis of (1), and $g^*H=0$.
