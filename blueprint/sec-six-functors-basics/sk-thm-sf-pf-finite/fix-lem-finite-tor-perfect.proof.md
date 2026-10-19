+++
kind  = "proof"
of    = "fix-lem-finite-tor-perfect"
+++
Put $C=M_{\bar y}$, using [def-weil-pbc-geometric-stalks].
Constructibility in [def-weil-finite-torsion-constructibility]
makes each $H^r(C)$ finite over $\Lambda$, and only finitely
many are nonzero. Choose $[a,b]$ as in
[def-weil-finite-tor-amplitude]. For an arbitrary
$\Lambda$-module $N$, use its constant sheaf $\underline N$
on $Y$. The exact stalk functor commutes with the
[def-weil-derived-tensor] derived tensor product, so

$$
H^r(C\otimes_\Lambda^L N)
=\mathcal H^r(M\otimes_\Lambda^L\underline N)_{\bar y}=0
\qquad(r\notin[a,b]).
$$

Taking $N=\Lambda$ also gives $H^r(C)=0$ outside $[a,b]$.

The ring $\Lambda=\mathcal O_E/\pi_E^n$ is Noetherian and local.
Construct a bounded-above finite-free resolution $P^\bullet\to C$
with $P^r=0$ for $r>b$. The construction proceeds downwards:
choose finitely many generators of the highest cohomology, lift
them to cycles, and map a finite free module in that degree to a
representative of $C$. The cone has zero cohomology in that degree
and finitely generated cohomology in lower degrees; Noetherianity
ensures finite generation of the new kernels. Repeating this step
constructs the resolution, which stabilizes in each fixed degree.
Being bounded above and free, $P^\bullet$ is K-flat.

Put $Q=\operatorname{coker}(P^{a-1}\xrightarrow{d^{a-1}}P^a)$.
Since $H^r(P^\bullet)=0$ for $r<a$, the augmented sequence

$$
\cdots\longrightarrow P^{a-2}\longrightarrow P^{a-1}
\longrightarrow P^a\longrightarrow Q\longrightarrow0
$$

is a free resolution of $Q$. Hence, for every $\Lambda$-module
$N$, with no finiteness restriction,

$$
\operatorname{Tor}^{\Lambda}_1(Q,N)
=
\frac{\ker(P^{a-1}\otimes N\longrightarrow P^a\otimes N)}
{\operatorname{im}(P^{a-2}\otimes N\longrightarrow P^{a-1}\otimes N)}
=H^{a-1}(P^\bullet\otimes_\Lambda N)=0.
$$

Thus $Q$ is flat. It is finitely presented, as a cokernel of
finite free modules, so is projective and therefore finite free
over the local ring $\Lambda$. The differential $d^a$ factors
through $Q$, and the quotient map to

$$
0\longrightarrow Q\longrightarrow P^{a+1}
\longrightarrow\cdots\longrightarrow P^b\longrightarrow0
$$

with $Q$ in degree $a$ is a quasi-isomorphism.
This proves the finite-coefficient assertion on either site.

At a field coefficient $\Lambda\in\{E,\Qlb\}$, the pullback $\bar y^*K$ lies
in $\Dbc(\bar y,\Lambda)$, and its cohomology sheaves are the constructible
sheaves $\bar y^*H^r(K)$, locally free of finite rank
([sk-lem-coefficient-heart]). Hence
$C=\operatorname{Fib}(\bar y^*K)$ is a bounded complex of $\Lambda$-vector
spaces with finite-dimensional cohomology
([def-weil-finite-coefficient-point]). Splitting cycles and boundaries as
vector subspaces gives $\bigoplus_r H^r(C)[-r]\xrightarrow{\sim}C$, a finite
direct sum, which proves perfectness. No descent to a finite coefficient
field is needed for $\Lambda=\Qlb$.
