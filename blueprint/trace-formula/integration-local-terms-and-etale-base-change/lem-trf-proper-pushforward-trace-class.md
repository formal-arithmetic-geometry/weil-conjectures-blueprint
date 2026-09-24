+++
id = "lem-trf-proper-pushforward-trace-class"
kind = "remark"
title = "Proper pushforward compatibility of trace maps: discharged"
order = 3908
uses = ["def-trf-coefficient-pushforward", "lem-trf-trace-map-exchange", "lem-trf-trace-source-exchange", "thm-trf-trace-proper-compatibility"]
+++
Let $p:C'\to C$ be proper, $c_i'=c_i p$, and let
$u':Lc_2'^*K\to Rc_1'^!K$ be a correspondence on $C'$, with
pushforward correspondence $p_!u'$ and induced proper map
$p_F:F'\to F$ of fixed schemes. The compatibility

$$
\operatorname{Tr}_c(p_!u')=(p_F)_!\operatorname{Tr}_{c'}(u')
$$

is *proved* in this chapter: the coefficient pushforward
[def-trf-coefficient-pushforward] together with the exchange of
the trace-class sources [lem-trf-trace-source-exchange] and the
exchange of the trace maps [lem-trf-trace-map-exchange] assemble
to [thm-trf-trace-proper-compatibility] (Varshavsky,
[loc. cit.](https://arxiv.org/abs/math/0505564), 1.2.5). The
former open interface is therefore retired and is no longer listed
among the unresolved inputs of this chapter.
