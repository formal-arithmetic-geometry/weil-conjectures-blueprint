+++
id = "lem-sf-trace-base-change"
kind = "lemma"
title = "Base change for the trace"
order = 3960
uses = ["def-exchange-projection", "def-trf-admissibility", "lem-trf-trace-map-exchange", "lem-trf-trace-map-from-external-duality", "lem-trf-trace-source-exchange", "thm-sf-dual-base-change", "thm-sf-relative-trace"]
+++
In the setting of [def-sf-datum], let the Cartesian square of
[thm-sf-dual-base-change] have $f$ proper, so that $f'$ is proper and
the traces $\operatorname{tr}_f,\operatorname{tr}_{f'}$ of
[thm-sf-relative-trace] are defined. Then the two composites

$$
Lg^*Rf_*f^!\xrightarrow{\ Lg^*\operatorname{tr}_f\ }Lg^*,
\qquad
Lg^*Rf_*f^!\xrightarrow{\ \sim\ }Rf'_*f'^!Lg^*
\xrightarrow{\ \operatorname{tr}_{f'}\ }Lg^*
$$

agree, the isomorphism in the second being the exchange of
[def-exchange-projection] for the proper $f$ together with the canonical
identification of the exceptional pullbacks of the square.

## Proof

In the concrete setting this is a theorem of the trace-formula chapter, where
the trace is constructed: the exchange of the trace-class sources is
[lem-trf-trace-source-exchange], and the exchange of the trace maps is
[lem-trf-trace-map-exchange], whose proof identifies the coherence at
issue with the coherence datum relating the exchange to the ordinary units
and the exceptional counits, recorded in [def-trf-admissibility]. The
trace of [thm-sf-relative-trace] is the counit of $Rf_!\dashv Rf^!$, and
that counit is the categorical trace of the trace-formula chapter read
through the external duality [lem-trf-trace-map-from-external-duality];
the two displayed composites are therefore the two sides of that exchange,
and they agree.
