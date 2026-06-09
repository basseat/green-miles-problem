# The Green Miles Problem
## Germany Has the Ambition. The Data Has Questions.

---

Last time I left you with a question: Germany has some of the most ambitious climate targets in the world. It also runs one of the largest logistics operations in Europe. Can both be true at the same time?

I've spent the last few weeks trying to answer that with data. The short answer is: partly. The longer answer is more interesting.

There is a story Germany tells about itself, and the world largely accepts it. The Energiewende. The colour-coded recycling bins. The EU's environmental conscience. Germany is the country that takes climate seriously, the one whose industrial ambition comes wrapped in green credentials. That story is not made up. But it is incomplete in a specific way that the data makes visible.

**What I actually looked at**

I pulled road freight, transport emissions, waste recycling rates, and postal and parcel volumes for five comparable European economies (Germany, France, Spain, Netherlands, and Poland) going back to 2000. All of it came from the Eurostat API and the European Commission's postal statistics database. Three hypotheses. Does Germany's logistics operation outscale its neighbours? Does its transport sector emit disproportionately? And is the gap between its emissions and its mitigation efforts larger than the green reputation suggests?

**What the data shows**

The scale story is real. Germany's road freight averages 307,893 million tonne-kilometres a year. France, with a comparable population, averages 184,324 million TKM. Germany processes more than three times as many parcels per person as France. The infrastructure, the industrial base, and the consumer spending power are all pointing in the same direction.

But there is a twist in the freight numbers that I didn't expect going in.

Poland has overtaken Germany in road freight. Poland's volumes grew from 102,807 million TKM in 2000 to over 385,089 million TKM by the end of the study period. Nearshoring, manufacturing relocation, and two decades of logistics investment have quietly shifted the centre of gravity of European freight east. Businesses still treating Germany as the only anchor of their European supply chain are working with an outdated map. That struck me as the most commercially significant finding in the whole project.

On emissions, the hypothesis confirms cleanly. Germany's transport sector peaked at 182,200 million tonnes of CO₂ equivalent, the highest of all five countries and nearly 25% above France despite similar population sizes. The comparison to Spain is starker: Spain averages roughly 57% of Germany's transport emissions figure. The gap is not explained by population or territory alone. It reflects Germany's freight composition, its road dependency relative to rail, and the weight of its industrial goods mix.

Here is where the narrative starts to fray.

Germany's transport emissions have fallen 20.4% since 2000. That is real and it shouldn't be dismissed. But over the same period, waste recycling grew by just 8.7%, across twelve years. Between 2018 and 2022, recycling volumes actually declined slightly. The logistics scale kept growing. The parcel volumes roughly doubled. And the mitigation response, measured against that scale, has not kept pace.

**The more precise framing**

Germany doesn't have a climate problem. It has a proportionality problem.

The progress is real. A 20.4% emissions reduction while tripling parcel volumes over two decades is not nothing. The recycling infrastructure is more developed than most. The direction of travel is right.

But Germany's green narrative is built on the electricity generation story: solar panels, wind turbines, the Energiewende. And that story is largely true on its own terms. The transport sector is a different problem, and on that measure Germany is the highest emitter in its peer group, not a leader. When you hold a 20% emissions reduction against an 8.7% recycling growth rate, across a logistics operation of this scale, the gap between the reputation and the reality becomes hard to look past.

It is less that Germany is being dishonest and more that the story being told is about one part of the picture. The part that looks best.

**The quieter story**

The Netherlands barely features in the Germany climate conversation. It probably should. It has far lower transport emissions per unit of logistics output than anyone else in the comparison. It processes more waste per capita. It runs one of the world's largest port economies (Rotterdam) without the emissions profile that Germany's inland freight network produces. If you want a benchmark for where European logistics needs to get to, the Netherlands is the destination. Germany is the transition.

And Poland is the growth story nobody in European logistics is talking about loudly enough. The freight data has been telling that story for years.

**The full data**

The dashboard is on Tableau Public and everything (methodology, pipeline, and code) is on GitHub. As always, it's all open.

Next up: I want to look at something that moves differently to freight. Not goods. Not emissions. Beliefs. Specifically, I want to know why some of the world's major religions have spread across continents and others have barely moved from where they started. And why, in the last hundred years, one religion quietly relocated its entire centre of gravity to a different hemisphere. The numbers are stranger than the story you've been told.

---

*Data sources: Eurostat API (road freight, transport emissions, recycling rates, 2000–2024) and EC GROW Postal Statistics / IPC GrowPost CUBE (2012–2024). Full code and methodology: [github.com/basseat/green-miles-problem](https://github.com/basseat/green-miles-problem)*
