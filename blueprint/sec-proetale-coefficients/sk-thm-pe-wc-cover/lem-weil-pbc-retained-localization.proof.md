+++
kind  = "proof"
of    = "lem-weil-pbc-retained-localization"
+++
*1.* The map $R^w\to R_{[J]}$ is a localization, hence ind-Zariski, and
$R\to R^w$ is ind-Zariski by [lem-weil-pbc-w-localization-points]; compose
using [lem-weil-pbc-ind-etale-stability]. The spectrum of $R_{[J]}$ is
identified with the set of points of the w-local space
$\operatorname{Spec}R^w$ that generalize a point of the closed set
$V(JR^w)$. In a w-local space this set is closed, and a closed subspace of a
w-local space is w-local.

*2.* By [lem-weil-pbc-w-localization-points], $V(JR^w)$ maps bijectively to
$V(J)$ and $R/J\cong R^w/JR^w$. A prime of $R^w$ containing $JR^w$ lies over a
maximal ideal of $R$ and has the same residue field, since $R\to R^w$
identifies local rings; as in 3 below it is therefore maximal. These primes survive in
$R_{[J]}$ and are the points of $V(JR_{[J]})$; they are closed, and every
point of $\operatorname{Spec}R_{[J]}$ generalizes one of them, so they are
exactly the closed points. Finally $R^w/JR^w\to R_{[J]}/JR_{[J]}$ is the
localization of $R^w/JR^w$ at elements that are already units, hence an
isomorphism.

*3.* A prime $\mathfrak q$ of $B$ containing $IB$ lies over a maximal ideal
$\mathfrak m$ of $A$; since $B/\mathfrak q$ is a domain containing the field
$\kappa(\mathfrak m)$ whose fraction field is algebraic over it, $B/\mathfrak q$
is a field and $\mathfrak q$ is maximal. So $V(IB)$ consists of closed points
and 2 applies to $J=IB$. If $A\to B$ is faithfully flat, then
$A\to B_{[IB]}$ is flat by 1, and every maximal ideal $\mathfrak m\supset I$ of
$A$ is the image of a prime of $B$ containing $IB$, which by 2 is the image
of a point of $\operatorname{Spec}B_{[IB]}$. Since flat maps satisfy going
down and every prime of $A$ lies in a maximal ideal, $\operatorname{Spec}
B_{[IB]}\to\operatorname{Spec}A$ is surjective.
