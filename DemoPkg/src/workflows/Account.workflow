<?xml version="1.0" encoding="UTF-8"?>
<Workflow xmlns="http://soap.sforce.com/2006/04/metadata">
    <rules>
        <fullName>New account_Alert</fullName>
        <actions>
            <name>create_email_alert</name>
            <type>Alert</type>
        </actions>
        <active>true</active>
        <description>New account</description>
        <formula>true</formula>
        <triggerType>onAllChanges</triggerType>
    </rules>
</Workflow>
