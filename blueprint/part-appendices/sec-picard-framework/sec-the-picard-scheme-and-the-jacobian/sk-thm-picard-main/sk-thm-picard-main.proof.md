+++
kind = "proof"
of = "sk-thm-picard-main"
uses = ["sk-prop-picard-pic-split", "sk-thm-picard-f-representable", "sk-thm-picard-twist", "sk-thm-picard-rr", "sk-thm-picard-hilb-curves", "sk-thm-picard-perfect", "sk-def-picard-pic", "det-picard-main-degree", "det-picard-main-jacobian"]
+++
The preceding lemmas assume $C$ geometrically integral. This holds
because $\bar k/k$ is purely inseparable, so $C_{\bar k}\to C$ is a
homeomorphism and $C_{\bar k}$ is connected and smooth, hence integral.

Representability and smoothness are local, and they follow because
translates of the chart $F$ cover $\operatorname{Pic}_{C/k}$. Properness
and connectedness of the components are global properties, which
cannot be checked on an open cover. We obtain them from the Abel map
$D\mapsto\mathcal O_C(D)$, which maps the proper irreducible scheme
$H_g$ onto the component of degree $g$, and translation carries this
component to every other one.

Choose $P\in C(k)$. By Proposition [sk-thm-picard-f-representable] we have a
representable open subfunctor $F\subset\operatorname{Pic}_{C/k}$. For a fixed class
$M\in\operatorname{Pic}_{C/k}(k)$, the translate
$M^{-1}F$, consisting of the classes $\mathcal L$ with
$\mathcal L\otimes M$ in $F$, is another representable open
subfunctor. Given a class on a $k$-scheme $T$, we apply
Lemma [sk-thm-picard-twist] to its fibre over each residue field, and
we see that the open loci where the corresponding translated class lies
in $F$ cover $T$. Therefore these charts cover $\operatorname{Pic}_{C/k}$.
Their intersections are open in either chart, and their
transition isomorphisms satisfy the cocycle condition by functoriality.
Since an fppf sheaf covered by representable open subfunctors is
representable [Stacks, Tag 0B9Q](https://stacks.math.columbia.edu/tag/0B9Q), [Stacks, Tag 0B9Z](https://stacks.math.columbia.edu/tag/0B9Z), gluing the charts gives a scheme
representing $\operatorname{Pic}_{C/k}$.

For an invertible sheaf $\mathcal L$ on $C_T$, the Euler characteristic
$\chi(C_t,\mathcal L_t)$ is a locally constant function of $t\in T$,
because $C_T\to T$ is proper and flat. By Riemann–Roch, the degree of
$\mathcal L_t$ is therefore locally constant as well, and this defines the displayed decomposition into
open and closed pieces. The charts in $H_g$ and their translates show
that the scheme is smooth of dimension $g$. Since it is a group scheme
locally of finite type over a field, the unit section is a closed
immersion, because a $k$-rational point of such a scheme is closed. The
diagonal is the preimage of the unit section under
$(x,y)\mapsto xy^{-1}$, so it is closed, and hence the scheme is
separated.

The universal divisor defines the Abel map

$$
H_g\longrightarrow\operatorname{Pic}^g_{C/k},
\qquad D\longmapsto\mathcal O_C(D).
$$

For a line bundle $\mathcal L$ of degree $g$ on $C_{k'}$, with $k'$
algebraically closed, Riemann–Roch shows that $h^0(\mathcal L)\geq1$,
and hence this map is surjective. It follows that
$\operatorname{Pic}^g_{C/k}$ is quasi-compact, and since the charts are
locally of finite type, it is of finite type. Being separated of finite
type and the surjective image of the proper scheme $H_g$, it is proper.
For the same reason it is geometrically irreducible, because $H_g$ is.
Translation by $\mathcal O_C((d-g)P)$ identifies
$\operatorname{Pic}^g_{C/k}$ with the component of each degree $d$. In particular, the component of degree zero is smooth,
proper, connected and commutative, and hence it is an abelian variety
(see [Stacks, Tag 0BA0](https://stacks.math.columbia.edu/tag/0BA0)).

Finally, $T_0J(C)$ is the kernel of
$\operatorname{Pic}_{C/k}(k[\varepsilon])\to\operatorname{Pic}_{C/k}(k)$,
where $\varepsilon^2=0$. Since $\operatorname{Pic}(k[\varepsilon])=0$, this is
the kernel of $\operatorname{Pic}(C_{k[\varepsilon]})\to\operatorname{Pic}(C)$.
Because $\varepsilon^2=0$, the map $a\mapsto1+\varepsilon a$ is a homomorphism,
and it gives an exact sequence of sheaves of groups on $C$

$$
0\longrightarrow\mathcal O_C\longrightarrow
\mathcal O_{C_{k[\varepsilon]}}^\times\longrightarrow\mathcal O_C^\times
\longrightarrow1,
$$

split by the inclusion $\mathcal O_C^\times\subset \mathcal O_{C_{k[\varepsilon]}}^\times$. Taking $H^1$, we see that the
kernel is $H^1(C,\mathcal O_C)$. This proves the assertion about the
tangent space.

For a field extension $k'/k$, the Picard functor of $C_{k'}$ is the
restriction of $\operatorname{Pic}_{C/k}$ to $k'$-schemes, and hence its
representing scheme is the base change. Since the degree of
$\mathcal L_t$ is computed on the fibre $C_t$, the decomposition by
degree, and hence $J(C)$, is compatible with this base change.
