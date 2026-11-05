+++
kind = "proof"
of = "lemma-integral-model-weakly-contractible"
order = 242
+++
The hypothesis gives an isomorphism $(P^\bullet/\pi_E^n)_W\simeq K_n$ at
each level $n$, but these isomorphisms need not be compatible with the
reduction maps, so they do not assemble to a map into
$K=R\varprojlim_nK_n$. What we need is a compatible family of maps, that
is, an element of the inverse limit of the Hom groups between the
reductions. Such an element lifts to a map
$\mathcal O_{E,W}\otimes_{\mathcal O_E}P^\bullet\to K$, because $K$ is derived
complete. To find one that is an isomorphism at level $1$, we show that
these Hom groups satisfy the Mittag–Leffler condition with a rate $e$
independent of $n$. Derived Nakayama then shows that the lift is an
isomorphism.

Consider the tower of complexes

$$
\cHom_{(\mathcal O_E/\pi_E^n)_W}\bigl((P^\bullet/\pi_E^n)_W,K_n\bigr)
\in D(W_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n),
$$

with transition maps induced by the reduction maps $K_{n+1}\to K_n$, and
the tower of groups
$\Hom_{D(W_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)}\bigl((P^\bullet/\pi_E^n)_W,K_n\bigr)$
obtained by applying $H^0R\Gamma(W,-)$. Since $P^\bullet$ is finite
free, the first tower is the tower of reductions of
$(\mathcal O_{E,W}\otimes_{\mathcal O_E}(P^\bullet)^\vee)\otimes^{\mathbf L}_{\mathcal O_{E,W}}K$.

These Hom groups can be infinite, so the Mittag–Leffler condition
has to come from a uniform bound. Let $Q^\bullet=(P^\bullet)^\vee\otimes_{\mathcal O_E}P^\bullet$
and choose $e$ such that $\pi_E^e$ kills the torsion of
$H^1(Q^\bullet)$. Let $N\ge m\ge n+e$ and choose one isomorphism
$(P^\bullet/\pi_E^N)_W\simeq K_N$. Its reductions to levels $m$ and
$n$ identify the three internal Hom complexes at levels $N\to m\to n$
with the constant complexes
$Q^\bullet/\pi_E^N\to Q^\bullet/\pi_E^m\to Q^\bullet/\pi_E^n$. Their
zeroth cohomology sheaves are therefore the constant sheaves on the groups
$H^0(Q^\bullet/\pi_E^N)\to H^0(Q^\bullet/\pi_E^m)\to H^0(Q^\bullet/\pi_E^n)$.
By Lemma [lemma-images-cohomology-finite-levels] the images from levels $N$
and $m$ at level $n$ agree, as subsheaves. Since $W$ is weakly
contractible, taking sections over $W$ is exact, and so it commutes with
taking cohomology and images. Hence the images in the Hom group at level $n$
from levels $N$ and $m$ coincide as well. Since $e$ does not depend on
$n$, $m$ or $N$, we obtain the Mittag–Leffler condition: for every $n$ the
images at level $n$ are constant from level $n+e$ on.

To lift, note that each Hom group contains an isomorphism, and its
reduction to level $1$ is again an isomorphism. The stable image at
level $1$ is the image from level $1+e$, so it contains an invertible
class. By the Mittag–Leffler property this class lifts to a compatible
family $(\varphi_n)_n$ in the inverse limit of the Hom groups. The
Milnor sequence gives a surjection

$$
\begin{aligned}
&H^0R\varprojlim_n R\Gamma\bigl(W,\cHom_{(\mathcal O_E/\pi_E^n)_W}
((P^\bullet/\pi_E^n)_W,K_n)\bigr)\\
&\qquad\longrightarrow
\varprojlim_n\Hom_{D(W_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)}
\bigl((P^\bullet/\pi_E^n)_W,K_n\bigr),
\end{aligned}
$$

whose source is
$\Hom_{D(W_{\mathrm{pro}\acute{e}t},\mathcal O_E)}(\mathcal O_{E,W}\otimes_{\mathcal O_E}P^\bullet,K)$.
This holds because derived sections commute with inverse limits, $K$ is complete, and
tensoring with the finite free dual of $P^\bullet$ commutes with
inverse limits. The family $(\varphi_n)$ therefore lifts to a morphism
$\mathcal O_{E,W}\otimes_{\mathcal O_E}P^\bullet\to K$ whose first reduction is an isomorphism.
Since both objects are complete, derived Nakayama
(Lemma [lemma-reduction-derived-nakayama]) shows that this morphism is an
isomorphism. Here completeness of the source follows termwise from
$\mathcal O_{E,W}=\varprojlim(\mathcal O_E/\pi_E^n)_W$. Indeed, the
transition maps are epimorphisms, so this limit agrees with the
derived limit by Proposition [proposition-milnor-sequence].
