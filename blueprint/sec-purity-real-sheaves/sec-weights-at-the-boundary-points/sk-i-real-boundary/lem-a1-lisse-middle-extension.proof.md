+++
kind  = "proof"
of    = "lem-a1-lisse-middle-extension"
uses = ["lem-wf-boundary-stalk-invariants", "lem-wf-lisse-stalk-vanishing", "sk-lem-coefficient-heart", "sk-prop-pe-condensed-point", "det-prop-sfb-module-pullback-exact-main", "sk-thm-sf-ctf-stability"]
+++
The assertion is clear on $U_0$. At a removed point, lissity on
$C_0$ makes the local inertia action trivial, so the invariant-stalk
formula of [lem-wf-boundary-stalk-invariants] identifies the
target stalk with the original stalk: $(j_*j^*\mathcal F)_{\bar x}= ((j^*\mathcal F)_{\bar\eta})^{I_x}=(\mathcal F_{\bar x})^{I_x}= \mathcal F_{\bar x}$, the last equality because $I_x$ acts trivially
on the stalk of a lisse sheaf. The map is the naturality of the
adjunction at every geometric point. Both sides are constructible
($Rj_*$ preserves $\Dbc(-,\Qlb)$, [sk-thm-sf-ctf-stability]), so the kernel and the
cokernel of the map are constructible ([sk-lem-coefficient-heart] (1)). Geometric stalks are
exact (the pullback to a geometric point is exact, [det-prop-sfb-module-pullback-exact-main], and
its global sections are exact because every pro-étale cover of the spectrum of an
algebraically closed field has a section, [sk-prop-pe-condensed-point]), so the kernel and the
cokernel have zero stalks. A constructible $M$ with zero stalks vanishes: for each stratum
$a:S\hookrightarrow C$ of the filtration of [sk-lem-coefficient-heart] (3), $a^*M$ is lisse
with zero stalks, hence $a^*M=0$ by [lem-wf-lisse-stalk-vanishing] (2), so every subquotient
$a_!(a^*M)$ vanishes and $M=0$. Hence the map is an isomorphism.
