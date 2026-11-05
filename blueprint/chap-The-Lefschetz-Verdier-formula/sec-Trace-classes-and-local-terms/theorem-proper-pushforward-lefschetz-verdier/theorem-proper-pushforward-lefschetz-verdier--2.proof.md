+++
kind = "proof"
of = "theorem-proper-pushforward-lefschetz-verdier--2"
order = 925005
uses = ["theorem-proper-pushforward-lefschetz-verdier--1", "definition-action-correspondence", "definition-pushforward-correspondence", "definition-trace-class-local-terms", "lemma-local-terms-point", "proposition-properties-trace", "proposition-composition-base-change-rf-shriek"]
+++
Since $X$ and $c_2$ are proper, $C$ is proper. Push the correspondence
forward along $(a_X,a_C)$ to the identity correspondence on $s$.
The ordinary half of the pushed coefficient map is the pullback unit
in the definition of $T_c(u)$, by the triangle identities. The
exceptional half is the composition isomorphism followed by the
counit for $c_1$. Thus the pushed coefficient map, read through
$Ra_{X!}\simeq Ra_{X*}$ and the identity inverse images on $s$, is
conjugate to $T_c(u)$ (`Correspondence.globalOperator_eq_pushforwardCoeff`).

Transport the right dual along $Ra_{X!}K\simeq Ra_{X*}K$ and use
invariance of trace under an isomorphism
([proposition-properties-trace]). The trace is now that of the
endomorphism on the point. By [lemma-local-terms-point], it is the
integral of the trace class of the pushed correspondence.
Apply [theorem-proper-pushforward-lefschetz-verdier--1] to identify this
class with the pushforward of $\operatorname{Tr}_c(u)$ along
$F\to s$. Integration is unchanged by proper pushforward
(`BorelMooreSection.integral_eq_integral_pushforward`), so the result
is $\int_F\operatorname{Tr}_c(u)$.
