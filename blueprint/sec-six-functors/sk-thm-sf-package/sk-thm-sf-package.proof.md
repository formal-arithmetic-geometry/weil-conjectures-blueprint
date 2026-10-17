+++
kind  = "proof"
of    = "sk-thm-sf-package"
uses = ["sk-thm-existence", "sk-thm-sfb-proper-base-change", "sk-thm-sbc-coefficients", "sk-prop-scalar-six", "sk-def-sf-kv-maps", "sk-prop-sf-biduality-general", "sk-prop-sf-existence", "sk-prop-sf-pf-coherence", "sk-thm-sf-comp-composition", "sk-thm-sf-ctf-stability", "sk-thm-sf-kunneth-verdier", "sk-thm-sf-verdier-exchange"]
+++
Every clause is one of the propositions of §§ *What the earlier chapters prove* or
§§ *What this section proves*, with the following assembly.
Clause (1) is fix-prop-adjunctions together with
[sk-thm-existence], [def-weil-exceptional-inverse-image] and
[thm-sf-ambient-adjoint-class]: for every admissible $\Lambda$ the right
adjoint of $Rf_!$ on $\Dctf$ exists by Brown representability on
$\operatorname{Loc}(\Dctf)$ ([sk-thm-existence]); for finite $\Lambda$ it
agrees with the étale adjoint transported along the comparison, the
preservation being [sk-prop-sf-rf-shriek-preservation] — enough for every clause
below, all of which are typed on the small categories
([sk-rem-sf-fullcd-scope]); the ambient half of (1) is conditional on the
ambient datum and is consumed by nothing. Clause (2) is [sk-prop-sf-cbc], [sk-thm-properbasechange] and
[sk-thm-smooth-base-change] respectively: the first is proved in Chapter 17, the second
in §[sec-proper-base-change], the third in §[sec-smooth-base-change],
and none of them uses anything proved
in this section except the definitions. The latter two are statements about
torsion sheaves; their bounded-below forms at $A_{E,n}$ are the truncation
dévissage thm:weil-pbc-bounded-below and
sbc-thm-bounded-below-derived-smooth-base-change, transported to the
pro-étale site along the comparison of [sk-prop-sf-comparison]. The forms
for every admissible $\Lambda$ on the condensed $\Dctf$ are
[sk-thm-sfb-proper-base-change] and [sk-thm-sbc-coefficients]: the integral
case by reduction modulo $\pi_E$ ([sk-prop-scalar-six]) and derived
Nakayama, the rational case by integral models, and $\Qlb$ by descent to a
finite $E$. The coherence of $\operatorname{Ex}_!$ is
fix-lem-exchanges. Clause (3) is the projection-formula
chain of §§ *What this section proves*: the finite case [sk-thm-sf-pf-finite] reduces to
the compact-support projection formula of the framework chapter,
[sk-thm-sf-pf-proetale] carries it from the étale to the pro-étale site for
finite $\Lambda$, and [sk-prop-sf-pf-reduction], [sk-thm-sf-pf-adic] and
[sk-thm-sf-pf-field] give it on $X_{\mathrm{pro\acute et}}$ for
$\mathcal O_E$, $E$ and $\Qlb$, with
[sk-prop-sf-pf-coherence] for the coherence. Clause (4) is
[sk-thm-nagata-compactification] and [sk-prop-nagata-sketch-comp-category]
for the compactifications themselves, and [sk-prop-sf-comp-coherence],
[sk-thm-sf-comp-composition], [sk-prop-sf-comp-proper] of
§§ *What this section proves* for the independence, the composition law and proper
coincidence. Clause (5) is
[sk-thm-smooth-purity] of §[sec-smooth-purity], with
[sk-prop-cohsm] for the tensor form and [sk-thm-purity-transport] for the
$\mathcal O_E$, $E$ and $\Qlb$ stages; it is what makes the orientation of
[sk-def-sf-orientation] a theorem. Its compatibility with composition and
with $\operatorname{Ex}_!$ is the composition and base-change compatibility
of [sk-thm-smooth-purity] and [sk-prop-cohsm] (G12), read through
[sk-lem-sf-mate]; its compatibility with $\alpha$ is the smooth step of the
proof of [sk-thm-sf-kunneth-verdier]. Clause (6) is
[sk-prop-sf-biduality-general] (Chapter 1), [sk-thm-sf-verdier-exchange]
and [sk-thm-sf-global-duality] and [sk-thm-sf-identification]
(§§ *What this section proves*, using [sk-thm-sf-tensor-hom]), with
[sk-prop-sf-dualizable-biduality], [sk-lem-sf-twist-interchange] and
[sk-thm-sf-dual-perfect] for the perfect case; the compatibility of
$\varepsilon$ with composition is obtained by pasting the tensor–Hom chain of
[sk-thm-sf-tensor-hom] for $f$ and for $g$, using the associativity pentagon
of [sk-prop-sf-pf-coherence] and [sk-lem-sf-mate]
(fix-prop-coherence). Clause (7) is
[sk-thm-sf-kunneth-relative], whose proof uses clause (2), clause (3)
(with the base-change clause of [sk-prop-sf-pf-coherence] for its
coherence), clause (4) and, for the typing of $\operatorname{PF}_g$, clause
(8)(iv). Clause (8) is [sk-thm-sf-ctf-stability], whose proof uses
[sk-lem-sf-flat-model], [sk-thm-sf-direct-image-tor-amplitude],
[sk-cor-sf-direct-image-ctf], [sk-thm-sf-hom-ctf],
[sk-prop-sf-finiteness], [sk-prop-sf-comparison] and
[sk-prop-sf-rf-shriek-preservation]. No clause assumes a property that is
not proved in the blueprint: the *Conditional on* lines of
[sk-prop-sf-existence], [sk-prop-sf-biduality-general] and
[sk-thm-sf-ctf-stability] are the
complete list of what is conditional, and they are restated in the ledger
below.
