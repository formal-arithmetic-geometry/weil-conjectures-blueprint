+++
id = "sk-thm-sf-direct-image-tor-amplitude"
kind = "section"
title = "Direct image with finite Tor amplitude"
order = 2310
uses = ["sk-lem-sf-flat-model", "sk-prop-sf-finiteness"]
+++
*Theorem (sketch).*

Let $f:X\to Y$ be separated of finite type, of finite-type $k$-schemes with
$\dim X\le d$, and let $K$ be a bounded constructible $A$-complex on
$X_{\Et}$ with finite Tor amplitude in $[a,b]$. Then $Rf_*K$ is bounded
constructible on $Y_{\Et}$ with finite Tor amplitude in $[a,b+2d]$.

## Proof

Take the bounded flat model $P$ of [sk-lem-sf-flat-model], so
$\mathcal H^q(K)=0$ outside $[a,b]$. Let $\kappa=A/(\varpi_E)$; the
truncation spectral sequence for the left exact direct image applied to
$K\otimes^L_A\kappa_X$ has
$E_2^{p,q}=R^pf_*\bigl(\mathcal H^q(K\otimes^L_A\kappa_X)\bigr)$ with
$q\in[a,b]$ and $p\le 2d$ by the uniform vanishing of $R^pf_*$ above
$2\dim X$ on *every* module sheaf, which is
thm:sc-finite-type-torsion-cd ([sk-prop-sf-finiteness]); hence
$\mathcal H^n(Rf_*(K\otimes^L_A\kappa_X))=0$ outside $[a,b+2d]$.
Constructibility of $Rf_*K$ is prop:sf-finiteness. The projection formula for
the finitely presented constant coefficient $\kappa$ ([sk-rem-sf-pf-done])
identifies
$(Rf_*K)\otimes^L_A\kappa_Y\cong Rf_*(K\otimes^L_A\kappa_X)$, and the residue
test lem:exc-residue-tor-test converts that concentration into finite Tor
amplitude of $Rf_*K$ in $[a,b+2d]$.

Uses: `\Cref{lem:sf-flat-model}`, `\Cref{prop:sf-finiteness}`, `lem:exc-residue-tor-test`, `thm:sc-finite-type-torsion-cd`
