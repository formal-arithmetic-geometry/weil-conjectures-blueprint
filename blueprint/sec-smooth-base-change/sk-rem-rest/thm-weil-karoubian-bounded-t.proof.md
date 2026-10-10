+++
kind  = "proof"
of    = "thm-weil-karoubian-bounded-t"
+++
By [lem-weil-karoubi-envelope-triangulated] the envelope $\mathcal
T^\natural=\Kar(\mathcal T)$ of [def-weil-karoubi-envelope] is triangulated
and, by [lem-weil-envelope-tstructure], carries the extended t-structure
$((\mathcal T^\natural)^{\le0},(\mathcal T^\natural)^{\ge0})$, which is
bounded because every object of $\mathcal T^\natural$ is a retract of an
object of $\mathcal T$, of finite t-amplitude in the bounded t-structure of
$\mathcal T$. We show that every $Y\in\mathcal T^\natural$ is isomorphic to
an object of $\mathcal T$; full faithfulness of $\mathcal T\to\mathcal
T^\natural$, which is [lem-weil-karoubi-envelope-fully-faithful], then makes
it an equivalence, and every idempotent of $\mathcal T$ splits because its
image in $\mathcal T^\natural$ splits in the envelope that is idempotent
complete by [lem-weil-karoubi-envelope-idempotent-complete], and a splitting
transported back through the equivalence splits it in $\mathcal T$.

Since the extended t-structure is bounded, replacing $Y$ by a shift (which
preserves the property of being isomorphic to an object of $\mathcal T$), we
may assume $Y\in(\mathcal T^\natural)^{\ge0}$. Let $n\ge0$ be minimal with
$Y\in(\mathcal T^\natural)^{\le n}$, and argue by induction on $n$.

If $n=0$, then $Y$ lies in the heart of $\mathcal T^\natural$, which by
[lem-weil-envelope-tstructure] is equivalent to $\Kar(\mathcal H(\mathcal
T))$; by [prop-weil-heart-abelian] the heart $\mathcal H(\mathcal T)$ is
abelian and hence idempotent complete, so $\Kar(\mathcal H(\mathcal
T))=\mathcal H(\mathcal T)$ via the canonical functor, and $Y$ is isomorphic
to an object of $\mathcal H(\mathcal T)\subset\mathcal T$.

Assume $n>0$. The top truncation triangle of [def-weil-t-structure] in
$\mathcal T^\natural$ is

$$
 A:=\tau^{\le n-1}Y\longrightarrow Y\longrightarrow
 B:=\mathcal H^n(Y)[-n]\longrightarrow A[1],
$$

with $A\in(\mathcal T^\natural)^{\ge0}\cap(\mathcal T^\natural)^{\le n-1}$
(the truncation triangle and $\mathcal T^\natural$'s $\ge0$-part being closed
under kernels in the triangulated sense: $Y,B\in(\mathcal T^\natural)^{\ge0}$
and the connecting morphism argument gives $A\in(\mathcal
T^\natural)^{\ge0}$). By the induction hypothesis $A$ is isomorphic to an
object of $\mathcal T$. By [lem-weil-envelope-tstructure] the object $\mathcal
H^n(Y)$ lies in the heart of $\mathcal T^\natural$, which is equivalent to
$\mathcal H(\mathcal T)$ by the $n=0$ case; hence $B$ is isomorphic to an
object of $\mathcal T$. Since $\mathcal T\to\mathcal T^\natural$ is fully
faithful, the connecting morphism $\delta:B\to A[1]$ is the image of a
morphism of $\mathcal T$. Complete $\delta$ to a distinguished triangle in
$\mathcal T$ and rotate it to obtain

$$
 A\longrightarrow C\longrightarrow B\overset{\delta}{\longrightarrow}A[1]
$$

with the displayed connecting morphism $\delta$. This triangle is
distinguished in $\mathcal T^\natural$ as well. It and the truncation
triangle are cone triangles for the same morphism $\delta$ in $\mathcal
T^\natural$, so by uniqueness of cones (any two cone triangles of a morphism
are isomorphic by a morphism of triangles whose first two components are
identities) there is an isomorphism of triangles fixing $A$ and $B$; in
particular $Y\cong C$ in $\mathcal T^\natural$, with $C\in\mathcal T$. This
completes the induction and the proof.
