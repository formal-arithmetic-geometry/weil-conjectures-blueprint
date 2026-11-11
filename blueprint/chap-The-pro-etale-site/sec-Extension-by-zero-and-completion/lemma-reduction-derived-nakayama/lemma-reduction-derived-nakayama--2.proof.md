+++
kind = "proof"
of = "lemma-reduction-derived-nakayama--2"
order = 210004
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--3", "lemma-stability--7", "lemma-stability--8", "proposition-topos-functoriality--1", "lemma-extremally-disconnected-covers--3", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "lemma-reduction-derived-nakayama--1"]
+++
The first assertion follows from the two-term resolution of
$(\mathcal O_E/\pi_E^n)_X$ in
Corollary [corollary-finite-quotients-their-transition-maps]. Tensoring $K$ with the short exact sequence
$0\to\pi_E^n\mathcal O_E/\pi_E^{n+1}\to\mathcal O_E/\pi_E^{n+1}\to
\mathcal O_E/\pi_E^n\to0$, whose first term is isomorphic to
$\mathcal O_E/\pi_E$, gives a triangle $K_1\to K_{n+1}\to K_n$. By
induction $K_1=0$ implies $K_n=0$ for all $n$. Then the derived limit of
the $K_n$ vanishes, and $K=0$ by completeness.

*Source:* the proof of Lemma [lemma-reduction-derived-nakayama].
