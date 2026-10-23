+++
kind  = "proof"
of    = "lem-galois-descent"
+++
Step 1: the covering. The single surjective etale morphism $g$ is an
etale covering of $Y$, hence an fpqc covering by
[lem-weil-pbc-fpqc-finer-than-etale].
Step 2: the functor. For $P$ in $\mathrm{F\acute Et}(Y)$ as in
[def-galois-categories], i.e. a finite etale $Y$-scheme in the
conventions of [def-weil-pbc-scheme-conventions], the base change
$P'=P\times_YY'$ is finite etale over $Y'$, and both pullbacks of $P'$ to
$Y''$ are identified with $P\times_YY''$; the resulting isomorphism
$\varphi$ satisfies the cocycle condition over $Y'''$, and base changes of
$Y$-morphisms are compatible with these data
([def-pd-descent-datum]).
Step 3: full faithfulness. Morphisms of schemes descend along fpqc
coverings: for $P,Q$ over $Y$ the diagram
$\operatorname{Hom}_Y(P,Q)\to\operatorname{Hom}_{Y'}(P',Q')
\rightrightarrows\operatorname{Hom}_{Y''}(P'',Q'')$ is an equalizer
(affine-locally this is the exactness of $A\to A'\rightrightarrows A''$
for faithfully flat $A\to A'$). So compatible maps between the base
changes descend uniquely.
Step 4: essential surjectivity. A finite morphism is affine, and descent
data on schemes affine over the base are effective along fpqc coverings
(affine-locally this is faithfully flat descent of algebras). This
gives a $Y$-scheme $P$, affine over $Y$, with $P\times_YY'\cong P'$
compatibly with the descent data. Since $P\times_YY'\to Y'$ is finite
and etale, $P\to Y$ is finite by [lem-weil-pbc-fpqc-descend-finite] and
etale since being etale also descends along fpqc coverings. Hence $P$
lies in $\mathrm{F\acute Et}(Y)$.
Step 5: choosing such preimages, full faithfulness supplies a
quasi-inverse on morphisms and makes the chosen isomorphisms natural, so
base change is an equivalence.
