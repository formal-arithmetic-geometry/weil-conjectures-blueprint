+++
kind = "proof"
of = "sk-prop-diagonal-tower"
uses = ["sk-lem-geo-cartier", "sk-prop-pe-replete", "sk-prop-pe-products", "sk-prop-geo-p1-adjunction", "sk-cor-pe-bounded-continuity", "sk-prop-sfb-cartesian-coefficients"]
+++
The diagonal is an effective Cartier divisor, which gives a boundary morphism
$\Delta_*\mathbf Z\to\mathbf G_m[1]$ ([sk-lem-geo-cartier]). Tensoring with the
system $(\mathbf Z/\ell^n)_n$ and using the Kummer sequence, we get one morphism of
systems $\Delta_*\mathbf Z/\ell^\bullet\to\mathbf Z/\ell^\bullet(1)[2]$, and we take
$R\varprojlim$. Since the site is replete with exact products ([sk-prop-pe-replete]
and [sk-prop-pe-products]), $R\varprojlim\circ(-\otimes\mathbf Z/\ell^\bullet)$ is
derived $\ell$-completion ([Stacks, Tag 099M](https://stacks.math.columbia.edu/tag/099M)),
so the limit $\Delta_*\Zl\to\Zl(1)[2]$ is the completion of the boundary map of
[sk-lem-geo-cartier]; it is linear over the completed coefficient sheaf by
[Stacks, Tag 099I](https://stacks.math.columbia.edu/tag/099I). The trace comes in the
same way from the decomposition of $Rq_*\mathbf Z/\ell^\bullet$. Each
$\operatorname{Tr}_{p_i}\circ Rp_{i*}(\delta)$ is an endomorphism of
$\mathbf Z/\ell^\bullet$ in degree $0$, that is, a family of endomorphisms of the
levels, and these are the identity by [sk-prop-geo-p1-adjunction]. We then extend
scalars to $\mathcal O_E$, invert $\ell$ and take the colimit over finite extensions
([sk-cor-pe-bounded-continuity]). Base change holds since the Cartier and Kummer maps
are natural and pullback commutes with $R\varprojlim$ here
([sk-prop-sfb-cartesian-coefficients]).
