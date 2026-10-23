+++
kind = "proof"
of = "sk-thm-curve-package"
uses = ["sk-prop-sf-comparison", "sk-thm-br", "sk-thm-curveestimate", "sk-prop-curve-affine-kummer", "sk-prop-curve-artin-schreier", "sk-lem-curve-affine-artin-schreier", "sk-lem-curve-finite-support", "sk-lem-curve-normalization", "sk-lem-curve-dense-open", "sk-lem-curve-sylow-trace"]
+++
*Overview.* The proof has three stages. First, for constant coefficients on a
smooth connected curve the cohomology is computed explicitly: by the Kummer
sequence and the Jacobian for primes invertible in $k$
([sk-thm-br], [sk-thm-curveestimate], [sk-prop-curve-affine-kummer]), and by
the Artin–Schreier sequence and coherent cohomology for the characteristic
prime ([sk-prop-curve-artin-schreier], [sk-lem-curve-affine-artin-schreier]).
The rest of the proof reduces to these calculations. Second, normalization
and removal of finitely many points change the sheaf only by sheaves
supported on finitely many points. Since these have no higher cohomology,
they change $H^0$ and $H^1$ by finite groups and leave the higher degrees
unchanged ([sk-lem-curve-finite-support], [sk-lem-curve-normalization],
[sk-lem-curve-dense-open]). Third, a constructible torsion sheaf is the sum of
its primary parts, and each $r$-primary part has a filtration by
constructible $\mathbf F_r$-sheaves. On a dense smooth open, a finite
$\mathbf F_r$-local system $L$ becomes a successive extension of constant
sheaves after pullback along a finite étale cover $\pi$ of degree prime to
$r$, and the trace of $\pi$, divided by the degree, exhibits $L$ as a direct
summand of $\pi_*\pi^*L$ ([sk-lem-curve-sylow-trace]). Extensions and
filtered colimits then give the result for all torsion sheaves.

*Stability under extensions.* The assertions $(C_1)$–$(C_8)$
([def-weil-pbc-eight-curve-assertions]) pass along short exact sequences. To see
this, let $0\to F_1\to F\to F_2\to0$ be
exact, with the assertions known for $F_1$ and $F_2$. Vanishing and
finiteness follow from the long exact sequence, and invariance under field
extension from the map between the two long exact sequences and the five
lemma. For $(C_8)$, take $b\in H^2(U,F)$. Lift its image in $H^2(U,F_2)$ to
$c_2\in H^2(C,F_2)$. The obstruction to lifting $c_2$ to $H^2(C,F)$ lies in
$H^3(C,F_1)$, which vanishes by $(C_1)$. After choosing a lift $c$, the
difference $b-c|_U$ comes from $H^2(U,F_1)$, and $(C_8)$ for $F_1$ lifts this
difference. Adding that lift to $c$ gives the required global class (Stacks,
Tag 0A5C).

*Proof of the theorem.* By [sk-prop-sf-comparison] we may work on
$C_{\mathrm{ét}}$. A universal homeomorphism does not change the étale topos (Stacks,
Tag 03SI), so we may replace $C$ by
$C_{\mathrm{red}}$. A constructible torsion sheaf has a finite exponent,
because it has finitely many isomorphism types of finite stalks. It is the
direct sum of its finitely many primary parts, and a finite filtration of an
$r$-primary part has constructible $\mathbf F_r$-sheaves as graded pieces. By the stability
under extensions just proved, it suffices to treat such sheaves.

Choose a dense smooth open $j:U\hookrightarrow C$ on which the sheaf is
finite locally constant. [sk-lem-curve-dense-open] reduces to its extension
by zero. On the connected components of $U$, [sk-lem-curve-sylow-trace] and
finite direct image reduce to constant $\mathbf F_r$ extended by zero on
curves finite over $C$. Normalization ([sk-lem-curve-normalization]) and
[sk-lem-curve-finite-support] reduce these sheaves to the constant
calculations on smooth curves: the Kummer sequence for
$r\neq\operatorname{char}k$ ([sk-thm-curveestimate],
[sk-prop-curve-affine-kummer]) and the Artin–Schreier sequence for
$r=\operatorname{char}k$ ([sk-prop-curve-artin-schreier],
[sk-lem-curve-affine-artin-schreier]). All reductions preserve the hypothesis
that $C$ is proper or affine. This proves the theorem for constructible
torsion sheaves.

An arbitrary torsion sheaf on the qcqs scheme $C$ is a filtered colimit of
constructible torsion sheaves, and cohomology commutes with filtered colimits
(Stacks, Tags 03SA, 03Q5). For
torsion prime to the characteristic or $p$-primary torsion, the constructible
sheaves may be taken with the same kind of torsion, by splitting off primary
parts before passing to the colimit. Pullback and restriction also commute
with filtered colimits, so vanishing and the pullback isomorphisms pass to the
colimit. Surjectivity in $(C_8)$ passes to it because a representative of a
class already occurs at one stage. Finiteness is asserted only for
constructible sheaves. Finally [sk-prop-sf-comparison] returns these
conclusions and their maps to $C_{\mathrm{proét}}$.
