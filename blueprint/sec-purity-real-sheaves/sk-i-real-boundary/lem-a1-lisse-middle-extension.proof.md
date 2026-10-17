+++
kind  = "proof"
of    = "lem-a1-lisse-middle-extension"
+++
The assertion is clear on $U_0$. At a removed point, lissity on
$C_0$ makes the local inertia action trivial, so the invariant-stalk
formula of [lem-wf-boundary-stalk-invariants] identifies the
target stalk with the original stalk: $(j_*j^*\mathcal F)_{\bar x}= ((j^*\mathcal F)_{\bar\eta})^{I_x}=(\mathcal F_{\bar x})^{I_x}= \mathcal F_{\bar x}$, the last equality because $I_x$ acts trivially
on the stalk of a lisse sheaf. The map is the naturality of the
adjunction at every geometric point. Both sides are constructible
($Rj_*$ preserves $\Dbc(-,\Qlb)$, [sk-thm-sf-ctf-stability]), and geometric stalks are
jointly conservative on $\Cons(C,\Qlb)$: kernels and cokernels are constructible
([sk-lem-coefficient-heart] (1)), and a constructible sheaf with zero stalks has zero
stalks on each graded piece $a_!L$ of [sk-lem-coefficient-heart] (3), so each lisse $L$
vanishes. Hence the map is an isomorphism.
