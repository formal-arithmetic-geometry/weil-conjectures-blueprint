+++
kind = "proof"
of = "theorem-picard-scheme-jacobian-over-separably"
order = 1550
uses = ["definition-constructible-sheaves", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "lemma-coherent-base-change-invertible-sheaves", "theorem-hilbert-schemes-points-smooth-curve", "proposition-divisors-degree-g-open-chart", "lemma-twisting-h-0-1-h", "lemma-representability-picard-functor", "lemma-tangent-space-picard-functor"]
+++
Representability is Lemma [lemma-representability-picard-functor].
The tangent space is given by
Lemma [lemma-tangent-space-picard-functor]. Fix the point
$P\in C(k)$ used to define $F$.

For an invertible sheaf $\mathcal L$ on $C_T$, the Euler characteristic
$\chi(C_t,\mathcal L_t)$ is a locally constant function of $t\in T$.
This holds because $C_T\to T$ is proper and flat and $Rf_{T,*}\mathcal L$
is perfect (Lemma [lemma-coherent-base-change-invertible-sheaves]).
By Riemann–Roch the degree of $\mathcal L_t$ is locally constant as well.
This gives the displayed decomposition into open and closed pieces. The
charts in $\operatorname{Hilb}^{g}_{C/k}$ and their translates show
that the scheme is smooth of dimension $g$.

It remains to see that the scheme is separated. A $k$-rational point of a
scheme locally of finite type over a field is closed. Hence the unit
section of the group scheme is a closed immersion. The diagonal is the
preimage of the unit section under $(x,y)\mapsto xy^{-1}$, so it is
closed as well.

The universal divisor defines the Abel map

$$
\operatorname{Hilb}^{g}_{C/k}\longrightarrow\operatorname{Pic}^g_{C/k},
\qquad D\longmapsto\mathcal O_C(D).
$$

For a line bundle $\mathcal L$ of degree $g$ on $C_{k'}$, with $k'$
algebraically closed, Riemann–Roch gives
$h^0(\mathcal L)\geq\chi(\mathcal L)=g+1-g=1$. A nonzero section has an
effective divisor $D$ of degree $g$ with $\mathcal O(D)\simeq\mathcal L$.
Hence the Abel map is surjective on points over algebraically closed
fields, and this suffices for surjectivity. It follows that
$\operatorname{Pic}^g_{C/k}$ is quasi-compact. It is of finite type since
the charts are locally of finite type. A separated scheme of finite
type that is the surjective image of the proper scheme
$\operatorname{Hilb}^{g}_{C/k}$ is proper. It is geometrically irreducible
because $\operatorname{Hilb}^{g}_{C/k}$ is.
Translation by $\mathcal O_C((d-g)P)$ identifies
$\operatorname{Pic}^g_{C/k}$ with the component of each degree $d$. In
particular, the component of degree zero is smooth, proper, connected and
commutative. Such a group scheme is an abelian variety
(see [Stacks, [0BA0](https://stacks.math.columbia.edu/tag/0BA0)]).

The tangent space $T_0J(C)$ is the kernel of
$\operatorname{Pic}_{C/k}(k[\varepsilon])\to\operatorname{Pic}_{C/k}(k)$,
where $\varepsilon^2=0$. Since $\operatorname{Pic}(k[\varepsilon])=0$, this is
the kernel of $\operatorname{Pic}(C_{k[\varepsilon]})\to\operatorname{Pic}(C)$,
which is $H^1(C,\mathcal O_C)$ by
Lemma [lemma-tangent-space-picard-functor].

For a field extension $k'/k$, the Picard functor of $C_{k'}$ is the
restriction of $\operatorname{Pic}_{C/k}$ to $k'$-schemes. Hence its
representing scheme is the base change. The degree of $\mathcal L_t$ is
computed on the fibre $C_t$, so the decomposition by degree, and with it
$J(C)$, is compatible with this base change.
