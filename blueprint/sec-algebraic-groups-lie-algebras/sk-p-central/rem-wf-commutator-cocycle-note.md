+++
id = "rem-wf-commutator-cocycle-note"
kind = "remark"
title = "The elementary commutator form of the central-element argument"
order = 2727
uses = ["prop-wf-positive-degree-centre"]
+++
The proof above is the elementary commutator form of the classical
argument: for $\zeta:=z^m$ centralizing $A=H_{\mathrm{geom}}^\circ$
with $[\gamma,\zeta]\in A$ for all $\gamma\in H_{\mathrm{geom}}$, the
two identities

$$
\eta_{a\gamma}=a\,\eta_\gamma\,a^{-1},\qquad \eta_{\gamma a}=\eta_\gamma
\qquad(a\in A,\ \gamma\in H_{\mathrm{geom}}),
$$

with $\eta_\gamma:=[\gamma,\zeta]$, force
$\eta_\gamma\in Z(A)$; the finiteness of the centre of the semisimple
group then gives $[\gamma,\zeta^N]=\eta_\gamma^N=1$ for
$N=|Z(A)|$, i.e. the centrality of a positive-degree power. This
replaces the cocycle $\varphi_g(n):=g\zeta^ng^{-1}\zeta^{-n}$ of the
source; cf. the workspace note *prop21\_elementary\_proof.md*,
Prop. 2.1(ii).
